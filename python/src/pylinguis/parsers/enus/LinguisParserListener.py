# Generated from LinguisParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LinguisParser import LinguisParser
else:
    from LinguisParser import LinguisParser

# This class defines a complete listener for a parse tree produced by LinguisParser.
class LinguisParserListener(ParseTreeListener):

    # Enter a parse tree produced by LinguisParser#block.
    def enterBlock(self, ctx:LinguisParser.BlockContext):
        pass

    # Exit a parse tree produced by LinguisParser#block.
    def exitBlock(self, ctx:LinguisParser.BlockContext):
        pass


    # Enter a parse tree produced by LinguisParser#statement.
    def enterStatement(self, ctx:LinguisParser.StatementContext):
        pass

    # Exit a parse tree produced by LinguisParser#statement.
    def exitStatement(self, ctx:LinguisParser.StatementContext):
        pass


    # Enter a parse tree produced by LinguisParser#assignment.
    def enterAssignment(self, ctx:LinguisParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LinguisParser#assignment.
    def exitAssignment(self, ctx:LinguisParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LinguisParser#identifierFunctionCall.
    def enterIdentifierFunctionCall(self, ctx:LinguisParser.IdentifierFunctionCallContext):
        pass

    # Exit a parse tree produced by LinguisParser#identifierFunctionCall.
    def exitIdentifierFunctionCall(self, ctx:LinguisParser.IdentifierFunctionCallContext):
        pass


    # Enter a parse tree produced by LinguisParser#printlnFunctionCall.
    def enterPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
        pass

    # Exit a parse tree produced by LinguisParser#printlnFunctionCall.
    def exitPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
        pass


    # Enter a parse tree produced by LinguisParser#printFunctionCall.
    def enterPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
        pass

    # Exit a parse tree produced by LinguisParser#printFunctionCall.
    def exitPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
        pass


    # Enter a parse tree produced by LinguisParser#assertFunctionCall.
    def enterAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
        pass

    # Exit a parse tree produced by LinguisParser#assertFunctionCall.
    def exitAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
        pass


    # Enter a parse tree produced by LinguisParser#sizeFunctionCall.
    def enterSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
        pass

    # Exit a parse tree produced by LinguisParser#sizeFunctionCall.
    def exitSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
        pass


    # Enter a parse tree produced by LinguisParser#ifStatement.
    def enterIfStatement(self, ctx:LinguisParser.IfStatementContext):
        pass

    # Exit a parse tree produced by LinguisParser#ifStatement.
    def exitIfStatement(self, ctx:LinguisParser.IfStatementContext):
        pass


    # Enter a parse tree produced by LinguisParser#ifStat.
    def enterIfStat(self, ctx:LinguisParser.IfStatContext):
        pass

    # Exit a parse tree produced by LinguisParser#ifStat.
    def exitIfStat(self, ctx:LinguisParser.IfStatContext):
        pass


    # Enter a parse tree produced by LinguisParser#elseIfStat.
    def enterElseIfStat(self, ctx:LinguisParser.ElseIfStatContext):
        pass

    # Exit a parse tree produced by LinguisParser#elseIfStat.
    def exitElseIfStat(self, ctx:LinguisParser.ElseIfStatContext):
        pass


    # Enter a parse tree produced by LinguisParser#elseStat.
    def enterElseStat(self, ctx:LinguisParser.ElseStatContext):
        pass

    # Exit a parse tree produced by LinguisParser#elseStat.
    def exitElseStat(self, ctx:LinguisParser.ElseStatContext):
        pass


    # Enter a parse tree produced by LinguisParser#functionDecl.
    def enterFunctionDecl(self, ctx:LinguisParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by LinguisParser#functionDecl.
    def exitFunctionDecl(self, ctx:LinguisParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by LinguisParser#forStatement.
    def enterForStatement(self, ctx:LinguisParser.ForStatementContext):
        pass

    # Exit a parse tree produced by LinguisParser#forStatement.
    def exitForStatement(self, ctx:LinguisParser.ForStatementContext):
        pass


    # Enter a parse tree produced by LinguisParser#whileStatement.
    def enterWhileStatement(self, ctx:LinguisParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by LinguisParser#whileStatement.
    def exitWhileStatement(self, ctx:LinguisParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by LinguisParser#idList.
    def enterIdList(self, ctx:LinguisParser.IdListContext):
        pass

    # Exit a parse tree produced by LinguisParser#idList.
    def exitIdList(self, ctx:LinguisParser.IdListContext):
        pass


    # Enter a parse tree produced by LinguisParser#exprList.
    def enterExprList(self, ctx:LinguisParser.ExprListContext):
        pass

    # Exit a parse tree produced by LinguisParser#exprList.
    def exitExprList(self, ctx:LinguisParser.ExprListContext):
        pass


    # Enter a parse tree produced by LinguisParser#boolExpression.
    def enterBoolExpression(self, ctx:LinguisParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#boolExpression.
    def exitBoolExpression(self, ctx:LinguisParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#numberExpression.
    def enterNumberExpression(self, ctx:LinguisParser.NumberExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#numberExpression.
    def exitNumberExpression(self, ctx:LinguisParser.NumberExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#notExpression.
    def enterNotExpression(self, ctx:LinguisParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#notExpression.
    def exitNotExpression(self, ctx:LinguisParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#orExpression.
    def enterOrExpression(self, ctx:LinguisParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#orExpression.
    def exitOrExpression(self, ctx:LinguisParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#unaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#unaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#powerExpression.
    def enterPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#powerExpression.
    def exitPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#eqExpression.
    def enterEqExpression(self, ctx:LinguisParser.EqExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#eqExpression.
    def exitEqExpression(self, ctx:LinguisParser.EqExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#andExpression.
    def enterAndExpression(self, ctx:LinguisParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#andExpression.
    def exitAndExpression(self, ctx:LinguisParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#inExpression.
    def enterInExpression(self, ctx:LinguisParser.InExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#inExpression.
    def exitInExpression(self, ctx:LinguisParser.InExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#stringExpression.
    def enterStringExpression(self, ctx:LinguisParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#stringExpression.
    def exitStringExpression(self, ctx:LinguisParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#expressionExpression.
    def enterExpressionExpression(self, ctx:LinguisParser.ExpressionExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#expressionExpression.
    def exitExpressionExpression(self, ctx:LinguisParser.ExpressionExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#addExpression.
    def enterAddExpression(self, ctx:LinguisParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#addExpression.
    def exitAddExpression(self, ctx:LinguisParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#compExpression.
    def enterCompExpression(self, ctx:LinguisParser.CompExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#compExpression.
    def exitCompExpression(self, ctx:LinguisParser.CompExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#nullExpression.
    def enterNullExpression(self, ctx:LinguisParser.NullExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#nullExpression.
    def exitNullExpression(self, ctx:LinguisParser.NullExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:LinguisParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:LinguisParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#multExpression.
    def enterMultExpression(self, ctx:LinguisParser.MultExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#multExpression.
    def exitMultExpression(self, ctx:LinguisParser.MultExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#listExpression.
    def enterListExpression(self, ctx:LinguisParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#listExpression.
    def exitListExpression(self, ctx:LinguisParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#inputExpression.
    def enterInputExpression(self, ctx:LinguisParser.InputExpressionContext):
        pass

    # Exit a parse tree produced by LinguisParser#inputExpression.
    def exitInputExpression(self, ctx:LinguisParser.InputExpressionContext):
        pass


    # Enter a parse tree produced by LinguisParser#list.
    def enterList(self, ctx:LinguisParser.ListContext):
        pass

    # Exit a parse tree produced by LinguisParser#list.
    def exitList(self, ctx:LinguisParser.ListContext):
        pass


    # Enter a parse tree produced by LinguisParser#indexes.
    def enterIndexes(self, ctx:LinguisParser.IndexesContext):
        pass

    # Exit a parse tree produced by LinguisParser#indexes.
    def exitIndexes(self, ctx:LinguisParser.IndexesContext):
        pass



del LinguisParser