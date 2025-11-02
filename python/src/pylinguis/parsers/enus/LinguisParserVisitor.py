# Generated from LinguisParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LinguisParser import LinguisParser
else:
    from LinguisParser import LinguisParser

# This class defines a complete generic visitor for a parse tree produced by LinguisParser.

class LinguisParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LinguisParser#block.
    def visitBlock(self, ctx:LinguisParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#statement.
    def visitStatement(self, ctx:LinguisParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#assignment.
    def visitAssignment(self, ctx:LinguisParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx:LinguisParser.IdentifierFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#printlnFunctionCall.
    def visitPrintlnFunctionCall(self, ctx:LinguisParser.PrintlnFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#printFunctionCall.
    def visitPrintFunctionCall(self, ctx:LinguisParser.PrintFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#assertFunctionCall.
    def visitAssertFunctionCall(self, ctx:LinguisParser.AssertFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#sizeFunctionCall.
    def visitSizeFunctionCall(self, ctx:LinguisParser.SizeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#ifStatement.
    def visitIfStatement(self, ctx:LinguisParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#ifStat.
    def visitIfStat(self, ctx:LinguisParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#elseIfStat.
    def visitElseIfStat(self, ctx:LinguisParser.ElseIfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#elseStat.
    def visitElseStat(self, ctx:LinguisParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#functionDecl.
    def visitFunctionDecl(self, ctx:LinguisParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#forStatement.
    def visitForStatement(self, ctx:LinguisParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#whileStatement.
    def visitWhileStatement(self, ctx:LinguisParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#idList.
    def visitIdList(self, ctx:LinguisParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#exprList.
    def visitExprList(self, ctx:LinguisParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#boolExpression.
    def visitBoolExpression(self, ctx:LinguisParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#subscriptExpression.
    def visitSubscriptExpression(self, ctx:LinguisParser.SubscriptExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#numberExpression.
    def visitNumberExpression(self, ctx:LinguisParser.NumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:LinguisParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#notExpression.
    def visitNotExpression(self, ctx:LinguisParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#orExpression.
    def visitOrExpression(self, ctx:LinguisParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:LinguisParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#powerExpression.
    def visitPowerExpression(self, ctx:LinguisParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#eqExpression.
    def visitEqExpression(self, ctx:LinguisParser.EqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#andExpression.
    def visitAndExpression(self, ctx:LinguisParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#inExpression.
    def visitInExpression(self, ctx:LinguisParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#stringExpression.
    def visitStringExpression(self, ctx:LinguisParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#expressionExpression.
    def visitExpressionExpression(self, ctx:LinguisParser.ExpressionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#addExpression.
    def visitAddExpression(self, ctx:LinguisParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#compExpression.
    def visitCompExpression(self, ctx:LinguisParser.CompExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#nullExpression.
    def visitNullExpression(self, ctx:LinguisParser.NullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:LinguisParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#multExpression.
    def visitMultExpression(self, ctx:LinguisParser.MultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#listExpression.
    def visitListExpression(self, ctx:LinguisParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguisParser#inputExpression.
    def visitInputExpression(self, ctx:LinguisParser.InputExpressionContext):
        return self.visitChildren(ctx)



del LinguisParser