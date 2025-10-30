# Get all the Python stdlib we need
import ast
import logging
import sys
from typing import Any, Dict, List, Optional

# Get the ANTLR4 bits we need
from antlr4 import InputStream, CommonTokenStream

# Get our base class from parsers
from .. import LinguisParserBase, EvaluationError

# Get our ANTLR-generated parser code
from .LinguisLexer import LinguisLexer
from .LinguisParser import LinguisParser
from .LinguisParserVisitor import LinguisParserVisitor

class ENUSParser(LinguisParserBase):
    """ A parser for US English Linguis code. """

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger()
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.setLevel(logging.INFO)
        self.logger.info("ENUSParser::__init__")

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
        def visitBlock(self, ctx:LinguisParser.BlockContext):
            statements = []

            childct = 0

            for child in ctx.getChildren():
                self.logger.info(f"Block child {childct}: {ctx.statement(childct)} {ctx.functionDecl(childct)}")
                statements.append(self.visit(child))
                childct += 1
            return statements


        # Visit a parse tree produced by LinguisParser#statement.
        def visitStatement(self, ctx:LinguisParser.StatementContext):
            retval = None

            if ctx.assignment() != None:
                retval = self.visitAssignment(ctx.assignment())
            elif ctx.forStatement() != None:
                retval = self.visitForStatement(ctx.forStatement())
            elif ctx.functionCall() != None:
                retval = self.visitFunctionCallExpression(ctx.functionCall())
            elif ctx.ifStatement() != None:
                retval = self.visitIfStatement(ctx.ifStatement())
            elif ctx.whileStatement() != None:
                retval = self.visitWhileStatement(ctx.whileStatement())
            else:
                raise Exception(f"Unrecognized statement: {ctx.getText()}")

            self.logger.info(f"Statement \"{ctx.getText()}\" -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#assignment.
        def visitAssignment(self, ctx:LinguisParser.AssignmentContext) -> ast.Assign:
            expr = self.visit(ctx.expression())

            id = str(ctx.Identifier())
            assign = ctx.Assign() # always "="

            retval = ast.Assign(targets=[ast.Name(id=id, ctx=ast.Store())], value=expr)
            self.logger.info(f"Assignment -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#identifierFunctionCall.
        def visitIdentifierFunctionCall(self, ctx:LinguisParser.IdentifierFunctionCallContext):
            self.logger.info("IdentifierFunctionCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#printlnFunctionCall.
        def visitPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
            self.logger.info("PrintlnCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#printFunctionCall.
        def visitPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
            self.logger.info("PrintCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#assertFunctionCall.
        def visitAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
            self.logger.info("AssertCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#sizeFunctionCall.
        def visitSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
            self.logger.info("SizeCall")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#ifStatement.
        def visitIfStatement(self, ctx:LinguisParser.IfStatementContext):

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

            # We need a count of how many nodes there are in this
            children = []
            for child in ctx.getChildren():
                children.append(child)

            self.logger.info(f"IfStatement -> {len(children)} branches")

            ifstat = self.visitIfStat(ctx.ifStat())
            lastnode = None

            if ctx.elseStat() != None:
                elsestat = self.visitElseStat(ctx.elseStat())

            return ifstat


        # Visit a parse tree produced by LinguisParser#ifStat.
        def visitIfStat(self, ctx:LinguisParser.IfStatContext):
            self.logger.info("visiting IfStat")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#elseIfStat.
        def visitElseIfStat(self, ctx:LinguisParser.ElseIfStatContext):
            self.logger.info("visiting ElseIfStat")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#elseStat.
        def visitElseStat(self, ctx:LinguisParser.ElseStatContext):
            self.logger.info("visiting Else Stat")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#functionDecl.
        def visitFunctionDecl(self, ctx:LinguisParser.FunctionDeclContext):
            self.logger.info("visiting FunctionDecl")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#forStatement.
        def visitForStatement(self, ctx:LinguisParser.ForStatementContext):
            self.logger.info("visiting For Statement")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#whileStatement.
        def visitWhileStatement(self, ctx:LinguisParser.WhileStatementContext):
            self.logger.info("visiting While Statement")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#idList.
        def visitIdList(self, ctx:LinguisParser.IdListContext):
            self.logger.info("visiting IdList")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#exprList.
        def visitExprList(self, ctx:LinguisParser.ExprListContext):
            self.logger.info("visiting ExprList")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#boolExpression.
        def visitBoolExpression(self, ctx:LinguisParser.BoolExpressionContext) -> ast.Constant:
            retval = None
            if self.parser.getTruthy(ctx.getText()):
                retval = ast.Constant(True, None)
            else:
                retval = ast.Constant(False, None)
            self.logger.info(f"BoolExpression -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#numberExpression.
        def visitNumberExpression(self, ctx:LinguisParser.NumberExpressionContext) -> ast.Constant:
            retval = None
            if ctx.getText().count(".") == 1:
                retval = ast.Constant(float(ctx.getText()), None)
            else:
                retval = ast.Constant(int(ctx.getText()), None)
            self.logger.info(f"NumberExpression -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#identifierExpression.
        def visitIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
            retval = ast.Name(ctx.getText(), ctx=ast.Load()) 
                # Store() will need to be set by another element in the AST later once it's clear which is needed
            self.logger.info(f"IdentifierExpression -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#notExpression.
        def visitNotExpression(self, ctx:LinguisParser.NotExpressionContext):
            self.logger.info("visiting Not Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#orExpression.
        def visitOrExpression(self, ctx:LinguisParser.OrExpressionContext):
            self.logger.info("visiting Or Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#unaryMinusExpression.
        def visitUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
            self.logger.info("visiting UnaryMinute Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#powerExpression.
        def visitPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
            self.logger.info("visiting Power Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#eqExpression.
        def visitEqExpression(self, ctx:LinguisParser.EqExpressionContext):
            self.logger.info("visiting Eq Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#andExpression.
        def visitAndExpression(self, ctx:LinguisParser.AndExpressionContext):
            self.logger.info("visiting And Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#inExpression.
        def visitInExpression(self, ctx:LinguisParser.InExpressionContext):
            self.logger.info("visiting In Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#stringExpression.
        def visitStringExpression(self, ctx:LinguisParser.StringExpressionContext) -> ast.Constant:
            text = str(ctx.getText())[1:-1]
            retval = ast.Constant(text, None)
            self.logger.info(f"StringExpression -> {retval}")
            return retval


        # Visit a parse tree produced by LinguisParser#expressionExpression.
        def visitExpressionExpression(self, ctx:LinguisParser.ExpressionExpressionContext):
            self.logger.info("visiting ExpressionExpression")
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
            self.logger.info(f"AddExpression -> {retval}")
            #return self.visitChildren(ctx)
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
            self.logger.info(f"CompExpression -> {retval}")
            #return self.visitChildren(ctx)
            return retval


        # Visit a parse tree produced by LinguisParser#nullExpression.
        def visitNullExpression(self, ctx:LinguisParser.NullExpressionContext):
            self.logger.info("visiting Null Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#functionCallExpression.
        def visitFunctionCallExpression(self, ctx:LinguisParser.FunctionCallExpressionContext):
            self.logger.info("visiting FuncCall Expression")
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
            self.logger.info(f"MultExpression -> {retval}")
            #return self.visitChildren(ctx)
            return retval


        # Visit a parse tree produced by LinguisParser#listExpression.
        def visitListExpression(self, ctx:LinguisParser.ListExpressionContext):
            self.logger.info("visiting List Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#inputExpression.
        def visitInputExpression(self, ctx:LinguisParser.InputExpressionContext):
            self.logger.info("visiting Input Expression")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#list.
        def visitList(self, ctx:LinguisParser.ListContext):
            self.logger.info("visiting List")
            return self.visitChildren(ctx)


        # Visit a parse tree produced by LinguisParser#indexes.
        def visitIndexes(self, ctx:LinguisParser.IndexesContext):
            self.logger.info("visiting Indexes")
            return self.visitChildren(ctx)


    def parse(self, code: str) -> ast.Module:
    #def parse(self, code: str, parsermethodname : str = "block") -> ast.Module:
        """ Parses the entire code into a Python Module node. """

        # TODO: Need to figure out if/how ANTLR4 supports Unicode

        input_stream = InputStream(code)
        lexer = LinguisLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LinguisParser(stream)

        # The simple way
        tree = parser.block()

        # The more complicated way, designed to allow for flexible invocation
        # of the parser from tests
        #parsermethod = parser.__getattribute__("block")
        #if parsermethod == None:
        #    raise Exception(f"You tried to invoke a parser method that doesn't exist: {parsermethodname}")
        #else:
        #    self.logger.info(f"Parsing a {parsermethodname} from the grammar")
        #tree = parsermethod()

        self.logger.info("Tree:")
        self.logger.info(tree.toStringTree(recog=parser))  # Debug print of parse tree

        visitor = ENUSParser.Visitor(self)
        nodes = visitor.visit(tree)
        module = ast.Module(body=nodes, type_ignores=[])
        ast.fix_missing_locations(module) 
            # The above is absolutely necessary, to fixup line numbers and locations
            # for the AST to be valid for compilation. Failure to fix them yields errors.

        return module

    
