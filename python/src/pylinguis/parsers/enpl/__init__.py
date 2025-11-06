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

class ENPLParser(ANTLRParserBase):
    """ A parser for US Pig Latin Linguis code. """

    def __init__(self) -> None:
        self.logger = logging.getLogger("parsers.enpl")
        self.logger.info("ENPLParser::__init__")

    def getLexer(self, input_stream : antlr4.InputStream) -> antlr4.Lexer:
        return LinguisLexer(input_stream)

    def getParser(self, stream : antlr4.CommonTokenStream) -> antlr4.Parser:
        return LinguisParser(stream)

    def getVisitor(self) -> antlr4.ParseTreeVisitor:
        return ENPLParser.Visitor(self)

    def getTruthy(self, text : str) -> bool:
        """Take the text and determine if it is a True or False literal value."""

        if text == "uetray": return True
        elif text == "alsefay": return False
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

            for stmt in statements:
                self.logger.debug(f"Block -> {ast.dump(stmt)}")

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
            retval = None

            name = ctx.getChild(0).getText()

            params = []
            if ctx.exprList() != None:
                params = self.visit(ctx.exprList())
            self.logger.debug(f"IdentifierFnCall params: {params}")
            
            retval = ast.Call(func=ast.Name(name), 
                                             args=params, 
                                             keywords=[ ])
            
            self.logger.debug(f"IdentifierFnCall -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#printlnFunctionCall.
        def visitPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
            retval = None
            param = None

            if ctx.expression() != None:
                param = self.visit(ctx.expression())
            
            retval = ast.Expr(value=ast.Call(func=ast.Name("print"), 
                                             args=[ param ]))
            
            self.logger.debug(f"Println -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#printFunctionCall.
        def visitPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
            retval = None
            param = None

            if ctx.expression() != None:
                param = self.visit(ctx.expression())
            
            retval = ast.Expr(value=ast.Call(func=ast.Name("print"), 
                                             args=[ param ], 
                                             keywords=[ ast.keyword(arg='end', value=ast.Constant(value='')) ]))
            
            self.logger.debug(f"Print -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#assertFunctionCall.
        def visitAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
            expr = self.visit(ctx.expression())
            retval = ast.Assert(expr, msg = ast.Constant(f"Assertion Failure: {ctx.expression().getText()}"))
            self.logger.debug(f"AssertCall -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#sizeFunctionCall.
        def visitSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
            retval = None

            target = self.visit(ctx.expression())
            retval = ast.Call(func=ast.Name("len"), args=[ target ])

            self.logger.debug(f"Size -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#ifStatement.
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
            retval = None

            name = str(ctx.getChild(1).getText())
            args = []
            if ctx.idList() != None:
                args = ast.arguments(self.visit(ctx.idList()))
            block = self.visit(ctx.block())
            self.logger.debug(f"FunctionDecl -> {name} {args} {block}")
            retval = ast.FunctionDef(name=name, args=args, body=block)

            self.logger.debug(f"FunctionDecl -> {ast.dump(retval)}")
            return retval


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
            retval = []
            for idx in range(0, ctx.getChildCount()):
                child = ctx.getChild(idx)
                retval.append(ast.arg(arg=child.getText()))
            self.logger.debug(f"IdList -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#exprList.
        def visitExprList(self, ctx:LinguisParser.ExprListContext):
            retval = None

            retval = []
            for idx in range(0, ctx.getChildCount()):
                child = ctx.expression(idx)
                if child != None:
                    childelt = self.visit(child)
                    self.logger.debug(f"ExprList childelt = {ast.dump(childelt) if childelt != None else "(None)"}")
                    retval.append(childelt)

            self.logger.debug(f"ExprList -> {retval}")
            return retval


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


        # Visit a parse tree produced by LinguisParser#subscriptExpression.
        def visitSubscriptExpression(self, ctx:LinguisParser.SubscriptExpressionContext):
            retval = None

            name = ctx.getChild(0).getText()
            value = self.visit(ctx.expression())

            retval = ast.Subscript(ast.Name(id=name), slice=value)

            self.logger.debug(f"SubscriptExpression -> {ast.dump(retval)}")
            return retval

        # Visit a parse tree produced by LinguisParser#identifierExpression.
        def visitIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
            retval = ast.Name(ctx.getText(), ctx=ast.Load()) 

            self.logger.debug(f"IdentifierExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#notExpression.
        def visitNotExpression(self, ctx:LinguisParser.NotExpressionContext):
            target = self.visit(ctx.expression())
            retval = ast.UnaryOp(op=ast.Not(), values=[ target ])
            self.logger.debug(f"NotExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#orExpression.
        def visitOrExpression(self, ctx:LinguisParser.OrExpressionContext):
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            retval = ast.BoolOp(op=ast.Or(), values=[ left, right ])
            self.logger.debug(f"AndExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#unaryMinusExpression.
        def visitUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
            target = self.visit(ctx.expression())
            retval = ast.UnaryOp(op=ast.USub(), values=[ target ])
            self.logger.debug(f"UnaryMinusExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#powerExpression.
        def visitPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
            retval = ast.BinOp(left=self.visit(ctx.base), right=self.visit(ctx.expo), op=ast.Pow())
            self.logger.debug(f"PowerExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#eqExpression.
        def visitEqExpression(self, ctx:LinguisParser.EqExpressionContext):
            op = None
            if ctx.Equals() != None:
                op = ast.Eq()
            elif ctx.NEquals() != None:
                op = ast.NotEq()
            else:
                raise Exception("Unknown operator in EqExpression")

            retval = ast.Compare(left=self.visit(ctx.left), comparators=[self.visit(ctx.right)], ops=[op])
            self.logger.debug(f"EqExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#andExpression.
        def visitAndExpression(self, ctx:LinguisParser.AndExpressionContext):
            retval = ast.BoolOp(op=ast.And(), values=[ self.visit(ctx.left), self.visit(ctx.right) ])
            self.logger.debug(f"AndExpression -> {ast.dump(retval)}")
            return retval


        # Visit a parse tree produced by LinguisParser#inExpression.
        def visitInExpression(self, ctx:LinguisParser.InExpressionContext):
            retval = ast.BoolOp(op=ast.In(), values=[ self.visit(ctx.left), self.visit(ctx.right) ])
            self.logger.debug(f"InExpression -> {ast.dump(retval)}")
            return retval


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
            retval = self.visit(ctx.functionCall())
            self.logger.debug(f"FuncCallExpression -> {ast.dump(retval)}")
            return retval


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
            retval = ast.List(elts=self.visit(ctx.exprList()))
            self.logger.debug(f"ListExpression -> {ast.dump(retval) if retval != None else "(None)"}")
            return retval


        # Visit a parse tree produced by LinguisParser#inputExpression.
        def visitInputExpression(self, ctx:LinguisParser.InputExpressionContext):
            retval = None

            prompt = ast.Constant("")
            if ctx.expression() != None:
                prompt = self.visit(ctx.expression())
            
            retval = ast.Call(func=ast.Name("input"), args=[ prompt ])

            self.logger.debug(f"InputExpression -> {ast.dump(retval) if retval != None else "(None)"}")
            return retval

