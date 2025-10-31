# Get all the Python stdlib we need
import ast
import logging
from typing import Any, Dict, List, Optional

# Get the ANTLR4 bits we need
import antlr4

# Get base-package elements we need
from .. import ANTLRParserBase, EvaluationError

# Get our ANTLR-generated parser code
from .LinguisLexer import LinguisLexer
from .LinguisParser import LinguisParser
from .LinguisParserVisitor import LinguisParserVisitor

class ENUSParser(ANTLRParserBase):
    """ A parser for US English Linguis code. """

    def __init__(self) -> None:
        self.logger = logging.getLogger("parsers.enus")
        self.logger.info("ENUSParser::__init__")

    def getLexer(self, input_stream : antlr4.InputStream) -> antlr4.Lexer:
        return LinguisLexer(input_stream)

    def getParser(self, stream : antlr4.CommonTokenStream) -> antlr4.Parser:
        return LinguisParser(stream)

    def getVisitor(self) -> antlr4.ParseTreeVisitor:
        return ENUSParser.Visitor(self)

    def builtins(self) -> Dict[str, Any]:
        """ 
        Returns a dictionary of built-in functions available in this parser's environment.
        This is necessary since the builtins are named values, and therefore need to have the
        language-dependent name for the binding. (Plus, I suppose, there could be builtins that
        are unique to each language for some reason, but I don't know what that would be.)
        """
        return { 
            "assert": lambda condition: condition or (_ for _ in ()).throw(EvaluationError("Assertion failed")),
            "input": lambda prompt=None: input(prompt) if prompt is not None else input(),
            "println": lambda *args: print(*args),
            "print": lambda *args: print(*args, end=""),
            "size": lambda lst: len(lst) if isinstance(lst, list) else 0,
        }

    def getTruthy(self, text : str) -> bool:
        if text == "true": return True
        elif text == "false": return False
        else: raise EvaluationError(f"{text} not recognized as a boolean value")

    class Visitor(LinguisParserVisitor):
        def __init__(self, parser) -> None:
            super().__init__()
            self.parser = parser
            self.logger = parser.logger

        # Visit a parse tree produced by LinguisParser#block.
        def visitBlock(self, ctx:LinguisParser.BlockContext) -> list[ast.AST]:
            statements = []
            
            for child in ctx.getChildren():
                if isinstance(child, LinguisParser.StatementContext):
                    node = self.visit(child)
                    statements.append(node)
                elif isinstance(child, LinguisParser.FunctionDeclContext):
                    node = self.visit(child)
                    statements.append(node)

            if ctx.Return() != None:
                ret_stmt = ast.Return(value=self.visit(ctx.expression()))
                self.logger.debug(f"Block has a return: {ast.dump(ret_stmt)}")
                statements.append(ret_stmt)

            self.logger.debug(f"Block -> {[ast.dump(s) for s in statements]}")
            return statements


        # Visit a parse tree produced by LinguisParser#statement.
        def visitStatement(self, ctx:LinguisParser.StatementContext) -> ast.Assign | ast.For | ast.Call | ast.If | ast.While:
            retval = None

            if ctx.assignment() != None:
                retval = self.visit(ctx.assignment())
                if retval == None:
                    self.logger.debug("Got None from self.visit()")
            elif ctx.forStatement() != None:
                retval = self.visit(ctx.forStatement())
                if retval == None:
                    self.logger.debug("Got None from self.visit()")
            elif ctx.functionCall() != None:
                retval = self.visit(ctx.functionCall())
                if retval == None:
                    self.logger.debug("Got None from self.visit()")
            elif ctx.ifStatement() != None:
                retval = self.visit(ctx.ifStatement())
                if retval == None:
                    self.logger.debug("Got None from self.visit()")
            elif ctx.whileStatement() != None:
                retval = self.visit(ctx.whileStatement())
                if retval == None:
                    self.logger.debug("Got None from self.visit()")
            else:
                raise Exception(f"Unrecognized statement: {ctx.getText()}")

            self.logger.debug(f"Statement \"{ctx.getText()}\" -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#assignment.
        def visitAssignment(self, ctx:LinguisParser.AssignmentContext) -> ast.Assign:
            expr = self.visit(ctx.expression())
            id = str(ctx.Identifier())

            retval = ast.Assign(targets=[ast.Name(id=id, ctx=ast.Store())], value=expr)
            self.logger.debug(f"Assignment -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#identifierFunctionCall.
        def visitIdentifierFunctionCall(self, ctx:LinguisParser.IdentifierFunctionCallContext):
            self.logger.debug("IdentifierFunctionCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#printlnFunctionCall.
        def visitPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
            self.logger.debug("PrintlnCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#printFunctionCall.
        def visitPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
            self.logger.debug("PrintCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#assertFunctionCall.
        def visitAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
            self.logger.debug("AssertCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#sizeFunctionCall.
        def visitSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
            self.logger.debug("SizeCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#ifStatement.
        # This one is a little tricky, since essentially Python wants to chain
        # each else off of a corresponding if, a la:
        #
        # if x:
        #     ...
        # elif y:
        #     ...
        # else:
        #     ...
        # 
        # Transforms into:
        # 
        # Module(
        #     body=[
        #         If(
        #             test=Name(id='x', ctx=Load()),
        #             body=[
        #                 Expr(
        #                     value=Constant(value=Ellipsis))],
        #             orelse=[
        #                 If(
        #                     test=Name(id='y', ctx=Load()),
        #                     body=[
        #                         Expr(
        #                             value=Constant(value=Ellipsis))],
        #                     orelse=[
        #                         Expr(
        #                             value=Constant(value=Ellipsis))])])])
        #
        def visitIfStatement(self, ctx:LinguisParser.IfStatementContext):
            retval = self.visit(ctx.ifStat())

            childct = ctx.getChildCount() - 1 # Last child is always 'end' node
            current = retval
            for idx in range(1, childct):     # First child is always 'if' node
                child = ctx.getChild(idx)
                if hasattr(child, "If") and hasattr(child, "Else"):
                    elseifnode = self.visitElseIfStat(child)
                    current.orelse = [ elseifnode ]
                    current = elseifnode
                elif hasattr(child, "Else"):
                    elsenode = self.visitElseStat(child)
                    current.orelse = elsenode
                    # No need to set current, we're at the end

            self.logger.info(f"IfStatement -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#ifStat.
        def visitIfStat(self, ctx:LinguisParser.IfStatContext) -> ast.If:
            test = self.visit(ctx.expression())
            stmts = self.visit(ctx.block())

            retval = ast.If(test=test, body=stmts, orelse=[])

            self.logger.debug(f"IfStat -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#elseIfStat.
        def visitElseIfStat(self, ctx:LinguisParser.ElseIfStatContext) -> ast.If:
            test = self.visit(ctx.expression())
            stmts = self.visit(ctx.block())

            retval = ast.If(test=test, body=stmts, orelse=[])

            self.logger.debug(f"ElseIfStat -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#elseStat.
        def visitElseStat(self, ctx:LinguisParser.ElseStatContext) -> List[ast.AST]:
            retval = self.visit(ctx.block())

            self.logger.debug(f"ElseStat -> {list(ast.dump(s) for s in retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#functionDecl.
        def visitFunctionDecl(self, ctx:LinguisParser.FunctionDeclContext):
            self.logger.debug("visiting FunctionDecl")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#forStatement.
        def visitForStatement(self, ctx:LinguisParser.ForStatementContext):
            retval = None
            
            identifier = ast.Name(ctx.getChild(1).getText(), ctx=ast.Store())

            start = self.visit(ctx.expression(0))
            end = self.visit(ctx.expression(1))
            # "for a = 0 to 3 do" -> "for a in range(0,3):"
            rangecall = ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[start,end])

            block = self.visit(ctx.block())

            retval = ast.For(target=identifier, 
                             iter=rangecall,
                             body=block)
            self.logger.debug(f"ForStatement -> {ast.dump(identifier)} {ast.dump(start)} {ast.dump(end)} {block}")
            return retval


        # Visit a parse tree produced by LinguisParser#whileStatement.
        def visitWhileStatement(self, ctx:LinguisParser.WhileStatementContext):
            retval = None
            test = self.visit(ctx.expression())
            block = self.visit(ctx.block())

            retval = ast.While(test, block, orelse=[])
            self.logger.debug(f"WhileStatement -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#idList.
        def visitIdList(self, ctx:LinguisParser.IdListContext):
            self.logger.debug("visiting IdList")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#exprList.
        def visitExprList(self, ctx:LinguisParser.ExprListContext):
            self.logger.debug("visiting ExprList")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#boolExpression.
        def visitBoolExpression(self, ctx:LinguisParser.BoolExpressionContext) -> ast.Constant:
            retval = None
            if self.parser.getTruthy(ctx.getText()):
                retval = ast.Constant(True, None)
            else:
                retval = ast.Constant(False, None)
            self.logger.debug(f"BoolExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#numberExpression.
        def visitNumberExpression(self, ctx:LinguisParser.NumberExpressionContext) -> ast.Constant:
            retval = None
            if ctx.getText().count(".") == 1:
                retval = ast.Constant(float(ctx.getText()), None)
            else:
                retval = ast.Constant(int(ctx.getText()), None)
            self.logger.debug(f"NumberExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#identifierExpression.
        def visitIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
            retval = ast.Name(ctx.getText(), ctx=ast.Load()) 
                # Store() will need to be set by another element in the AST later once it's clear which is needed
                # Actually I'm not sure that's true; it doesn't seem to be needed as I'm going through this, anyway....
            self.logger.debug(f"IdentifierExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#notExpression.
        def visitNotExpression(self, ctx:LinguisParser.NotExpressionContext):
            self.logger.debug("visiting Not Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#orExpression.
        def visitOrExpression(self, ctx:LinguisParser.OrExpressionContext):
            self.logger.debug("visiting Or Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#unaryMinusExpression.
        def visitUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
            self.logger.debug("visiting UnaryMinute Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#powerExpression.
        def visitPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
            self.logger.debug("visiting Power Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#eqExpression.
        def visitEqExpression(self, ctx:LinguisParser.EqExpressionContext):
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)

            op = None
            if ctx.Equals() != None:
                op = ast.Eq()
            elif ctx.NEquals() != None:
                op = ast.NotEq()
            else:
                raise Exception("Unknown operator in EqExpression")

            retval = ast.Compare(left=l, comparators=[r], ops=[op])
            self.logger.debug(f"EqExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#andExpression.
        def visitAndExpression(self, ctx:LinguisParser.AndExpressionContext):
            self.logger.debug("visiting And Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#inExpression.
        def visitInExpression(self, ctx:LinguisParser.InExpressionContext):
            self.logger.debug("visiting In Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#stringExpression.
        def visitStringExpression(self, ctx:LinguisParser.StringExpressionContext) -> ast.Constant:
            text = str(ctx.getText())[1:-1]
            retval = ast.Constant(text, None)
            self.logger.debug(f"StringExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#expressionExpression.
        def visitExpressionExpression(self, ctx:LinguisParser.ExpressionExpressionContext):
            self.logger.debug("visiting ExpressionExpression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#addExpression.
        def visitAddExpression(self, ctx:LinguisParser.AddExpressionContext) -> ast.BinOp:
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)

            op = None
            if ctx.Add() != None:
                op = ast.Add()
            elif ctx.Subtract() != None:
                op = ast.Sub()
            else:
                raise Exception("Unknown operator in AddExpression")

            retval = ast.BinOp(left=l, right=r, op=op)
            self.logger.debug(f"AddExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#compExpression.
        def visitCompExpression(self, ctx:LinguisParser.CompExpressionContext):
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)

            op = None
            if ctx.GT() != None:
                op = ast.Gt()
            elif ctx.GTEquals() != None:
                op = ast.GtE()
            elif ctx.LT() != None:
                op = ast.Lt()
            elif ctx.LTEquals() != None:
                op = ast.LtE()
            else:
                raise Exception("Unknown operator in CompExpression")

            retval = ast.Compare(left=l, comparators=[r], ops=[op])
            self.logger.debug(f"CompExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#nullExpression.
        def visitNullExpression(self, ctx:LinguisParser.NullExpressionContext):
            retval = ast.Constant(value=None)
            self.logger.debug(f"NullExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#functionCallExpression.
        def visitFunctionCallExpression(self, ctx:LinguisParser.FunctionCallExpressionContext):
            self.logger.debug("visiting FuncCall Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#multExpression.
        def visitMultExpression(self, ctx:LinguisParser.MultExpressionContext) -> ast.BinOp:
            l = self.visit(ctx.left)
            r = self.visit(ctx.right)

            op = None
            if ctx.Multiply() != None:
                op = ast.Mult()
            elif ctx.Divide() != None:
                op = ast.Div()
            elif ctx.Modulus() != None:
                op = ast.Mod()
            else:
                raise Exception("Unknown operator in MultExpression")

            retval = ast.BinOp(left=l, right=r, op=op)
            self.logger.debug(f"MultExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#listExpression.
        def visitListExpression(self, ctx:LinguisParser.ListExpressionContext):
            self.logger.debug("visiting List Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#inputExpression.
        def visitInputExpression(self, ctx:LinguisParser.InputExpressionContext):
            self.logger.debug("visiting Input Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#list.
        def visitList(self, ctx:LinguisParser.ListContext):
            self.logger.debug("visiting List")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#indexes.
        def visitIndexes(self, ctx:LinguisParser.IndexesContext):
            self.logger.debug("visiting Indexes")
            return self.visitChildren(ctx)

