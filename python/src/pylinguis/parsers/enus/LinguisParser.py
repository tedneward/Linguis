# Generated from LinguisParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,216,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,0,1,0,3,0,40,8,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,3,3,60,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,83,8,3,1,4,1,4,5,4,87,
        8,4,10,4,12,4,90,9,4,1,4,3,4,93,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,116,
        8,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,141,8,11,10,11,12,11,
        144,9,11,1,12,1,12,1,12,5,12,149,8,12,10,12,12,12,152,9,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,165,8,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,182,8,13,1,13,3,13,185,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,211,8,13,10,13,12,13,214,9,
        13,1,13,0,1,26,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,4,1,0,29,
        31,1,0,27,28,2,0,21,22,25,26,1,0,19,20,239,0,32,1,0,0,0,2,50,1,0,
        0,0,4,52,1,0,0,0,6,82,1,0,0,0,8,84,1,0,0,0,10,96,1,0,0,0,12,101,
        1,0,0,0,14,107,1,0,0,0,16,111,1,0,0,0,18,121,1,0,0,0,20,131,1,0,
        0,0,22,137,1,0,0,0,24,145,1,0,0,0,26,184,1,0,0,0,28,31,3,2,1,0,29,
        31,3,16,8,0,30,28,1,0,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,
        0,0,32,33,1,0,0,0,33,39,1,0,0,0,34,32,1,0,0,0,35,36,5,9,0,0,36,37,
        3,26,13,0,37,38,5,38,0,0,38,40,1,0,0,0,39,35,1,0,0,0,39,40,1,0,0,
        0,40,1,1,0,0,0,41,42,3,4,2,0,42,43,5,38,0,0,43,51,1,0,0,0,44,45,
        3,6,3,0,45,46,5,38,0,0,46,51,1,0,0,0,47,51,3,8,4,0,48,51,3,18,9,
        0,49,51,3,20,10,0,50,41,1,0,0,0,50,44,1,0,0,0,50,47,1,0,0,0,50,48,
        1,0,0,0,50,49,1,0,0,0,51,3,1,0,0,0,52,53,5,45,0,0,53,54,5,39,0,0,
        54,55,3,26,13,0,55,5,1,0,0,0,56,57,5,45,0,0,57,59,5,36,0,0,58,60,
        3,24,12,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,83,5,37,0,
        0,62,63,5,1,0,0,63,64,5,36,0,0,64,65,3,26,13,0,65,66,5,37,0,0,66,
        83,1,0,0,0,67,68,5,2,0,0,68,69,5,36,0,0,69,70,3,26,13,0,70,71,5,
        37,0,0,71,83,1,0,0,0,72,73,5,4,0,0,73,74,5,36,0,0,74,75,3,26,13,
        0,75,76,5,37,0,0,76,83,1,0,0,0,77,78,5,5,0,0,78,79,5,36,0,0,79,80,
        3,26,13,0,80,81,5,37,0,0,81,83,1,0,0,0,82,56,1,0,0,0,82,62,1,0,0,
        0,82,67,1,0,0,0,82,72,1,0,0,0,82,77,1,0,0,0,83,7,1,0,0,0,84,88,3,
        10,5,0,85,87,3,12,6,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,
        88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,93,3,14,7,0,92,91,1,
        0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,14,0,0,95,9,1,0,0,0,96,
        97,5,7,0,0,97,98,3,26,13,0,98,99,5,13,0,0,99,100,3,0,0,0,100,11,
        1,0,0,0,101,102,5,8,0,0,102,103,5,7,0,0,103,104,3,26,13,0,104,105,
        5,13,0,0,105,106,3,0,0,0,106,13,1,0,0,0,107,108,5,8,0,0,108,109,
        5,13,0,0,109,110,3,0,0,0,110,15,1,0,0,0,111,112,5,6,0,0,112,113,
        5,45,0,0,113,115,5,36,0,0,114,116,3,22,11,0,115,114,1,0,0,0,115,
        116,1,0,0,0,116,117,1,0,0,0,117,118,5,37,0,0,118,119,3,0,0,0,119,
        120,5,14,0,0,120,17,1,0,0,0,121,122,5,10,0,0,122,123,5,45,0,0,123,
        124,5,39,0,0,124,125,3,26,13,0,125,126,5,12,0,0,126,127,3,26,13,
        0,127,128,5,13,0,0,128,129,3,0,0,0,129,130,5,14,0,0,130,19,1,0,0,
        0,131,132,5,11,0,0,132,133,3,26,13,0,133,134,5,13,0,0,134,135,3,
        0,0,0,135,136,5,14,0,0,136,21,1,0,0,0,137,142,5,45,0,0,138,139,5,
        40,0,0,139,141,5,45,0,0,140,138,1,0,0,0,141,144,1,0,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,23,1,0,0,0,144,142,1,0,0,0,145,150,3,
        26,13,0,146,147,5,40,0,0,147,149,3,26,13,0,148,146,1,0,0,0,149,152,
        1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,25,1,0,0,0,152,150,1,
        0,0,0,153,154,6,13,-1,0,154,155,5,28,0,0,155,185,3,26,13,20,156,
        157,5,24,0,0,157,185,3,26,13,19,158,185,5,44,0,0,159,185,5,43,0,
        0,160,185,5,16,0,0,161,185,3,6,3,0,162,164,5,34,0,0,163,165,3,24,
        12,0,164,163,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,185,5,35,
        0,0,167,185,5,45,0,0,168,169,5,45,0,0,169,170,5,34,0,0,170,171,3,
        26,13,0,171,172,5,35,0,0,172,185,1,0,0,0,173,185,5,46,0,0,174,175,
        5,36,0,0,175,176,3,26,13,0,176,177,5,37,0,0,177,185,1,0,0,0,178,
        179,5,3,0,0,179,181,5,36,0,0,180,182,5,46,0,0,181,180,1,0,0,0,181,
        182,1,0,0,0,182,183,1,0,0,0,183,185,5,37,0,0,184,153,1,0,0,0,184,
        156,1,0,0,0,184,158,1,0,0,0,184,159,1,0,0,0,184,160,1,0,0,0,184,
        161,1,0,0,0,184,162,1,0,0,0,184,167,1,0,0,0,184,168,1,0,0,0,184,
        173,1,0,0,0,184,174,1,0,0,0,184,178,1,0,0,0,185,212,1,0,0,0,186,
        187,10,18,0,0,187,188,5,23,0,0,188,211,3,26,13,18,189,190,10,17,
        0,0,190,191,7,0,0,0,191,211,3,26,13,18,192,193,10,16,0,0,193,194,
        7,1,0,0,194,211,3,26,13,17,195,196,10,15,0,0,196,197,7,2,0,0,197,
        211,3,26,13,16,198,199,10,14,0,0,199,200,7,3,0,0,200,211,3,26,13,
        15,201,202,10,13,0,0,202,203,5,18,0,0,203,211,3,26,13,14,204,205,
        10,12,0,0,205,206,5,17,0,0,206,211,3,26,13,13,207,208,10,11,0,0,
        208,209,5,15,0,0,209,211,3,26,13,12,210,186,1,0,0,0,210,189,1,0,
        0,0,210,192,1,0,0,0,210,195,1,0,0,0,210,198,1,0,0,0,210,201,1,0,
        0,0,210,204,1,0,0,0,210,207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,
        0,0,212,213,1,0,0,0,213,27,1,0,0,0,214,212,1,0,0,0,16,30,32,39,50,
        59,82,88,92,115,142,150,164,181,184,210,212
    ]

class LinguisParser ( Parser ):

    grammarFileName = "LinguisParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'println'", "'print'", "'input'", "'assert'", 
                     "'size'", "'def'", "'if'", "'else'", "'return'", "'for'", 
                     "'while'", "'to'", "'do'", "'end'", "'in'", "'null'", 
                     "'||'", "'&&'", "'=='", "'!='", "'>='", "'<='", "'^'", 
                     "'!'", "'>'", "'<'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "'='", 
                     "','", "'?'", "':'" ]

    symbolicNames = [ "<INVALID>", "Println", "Print", "Input", "Assert", 
                      "Size", "Def", "If", "Else", "Return", "For", "While", 
                      "To", "Do", "End", "In", "Null", "Or", "And", "Equals", 
                      "NEquals", "GTEquals", "LTEquals", "Pow", "Excl", 
                      "GT", "LT", "Add", "Subtract", "Multiply", "Divide", 
                      "Modulus", "OBrace", "CBrace", "OBracket", "CBracket", 
                      "OParen", "CParen", "SColon", "Assign", "Comma", "QMark", 
                      "Colon", "Bool", "Number", "Identifier", "String", 
                      "Comment", "Space" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_functionCall = 3
    RULE_ifStatement = 4
    RULE_ifStat = 5
    RULE_elseIfStat = 6
    RULE_elseStat = 7
    RULE_functionDecl = 8
    RULE_forStatement = 9
    RULE_whileStatement = 10
    RULE_idList = 11
    RULE_exprList = 12
    RULE_expression = 13

    ruleNames =  [ "block", "statement", "assignment", "functionCall", "ifStatement", 
                   "ifStat", "elseIfStat", "elseStat", "functionDecl", "forStatement", 
                   "whileStatement", "idList", "exprList", "expression" ]

    EOF = Token.EOF
    Println=1
    Print=2
    Input=3
    Assert=4
    Size=5
    Def=6
    If=7
    Else=8
    Return=9
    For=10
    While=11
    To=12
    Do=13
    End=14
    In=15
    Null=16
    Or=17
    And=18
    Equals=19
    NEquals=20
    GTEquals=21
    LTEquals=22
    Pow=23
    Excl=24
    GT=25
    LT=26
    Add=27
    Subtract=28
    Multiply=29
    Divide=30
    Modulus=31
    OBrace=32
    CBrace=33
    OBracket=34
    CBracket=35
    OParen=36
    CParen=37
    SColon=38
    Assign=39
    Comma=40
    QMark=41
    Colon=42
    Bool=43
    Number=44
    Identifier=45
    String=46
    Comment=47
    Space=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.StatementContext)
            else:
                return self.getTypedRuleContext(LinguisParser.StatementContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(LinguisParser.FunctionDeclContext,i)


        def Return(self):
            return self.getToken(LinguisParser.Return, 0)

        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def SColon(self):
            return self.getToken(LinguisParser.SColon, 0)

        def getRuleIndex(self):
            return LinguisParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LinguisParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372092150) != 0):
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 4, 5, 7, 10, 11, 45]:
                    self.state = 28
                    self.statement()
                    pass
                elif token in [6]:
                    self.state = 29
                    self.functionDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 35
                self.match(LinguisParser.Return)
                self.state = 36
                self.expression(0)
                self.state = 37
                self.match(LinguisParser.SColon)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LinguisParser.AssignmentContext,0)


        def SColon(self):
            return self.getToken(LinguisParser.SColon, 0)

        def functionCall(self):
            return self.getTypedRuleContext(LinguisParser.FunctionCallContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(LinguisParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(LinguisParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(LinguisParser.WhileStatementContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LinguisParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                self.state = 42
                self.match(LinguisParser.SColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.functionCall()
                self.state = 45
                self.match(LinguisParser.SColon)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.whileStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)

        def Assign(self):
            return self.getToken(LinguisParser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LinguisParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(LinguisParser.Identifier)
            self.state = 53
            self.match(LinguisParser.Assign)
            self.state = 54
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LinguisParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssertFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Assert(self):
            return self.getToken(LinguisParser.Assert, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertFunctionCall" ):
                listener.enterAssertFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertFunctionCall" ):
                listener.exitAssertFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertFunctionCall" ):
                return visitor.visitAssertFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class SizeFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Size(self):
            return self.getToken(LinguisParser.Size, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeFunctionCall" ):
                listener.enterSizeFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeFunctionCall" ):
                listener.exitSizeFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeFunctionCall" ):
                return visitor.visitSizeFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class PrintlnFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Println(self):
            return self.getToken(LinguisParser.Println, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlnFunctionCall" ):
                listener.enterPrintlnFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlnFunctionCall" ):
                listener.exitPrintlnFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlnFunctionCall" ):
                return visitor.visitPrintlnFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)
        def exprList(self):
            return self.getTypedRuleContext(LinguisParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierFunctionCall" ):
                listener.enterIdentifierFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierFunctionCall" ):
                listener.exitIdentifierFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierFunctionCall" ):
                return visitor.visitIdentifierFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class PrintFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Print(self):
            return self.getToken(LinguisParser.Print, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunctionCall" ):
                listener.enterPrintFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunctionCall" ):
                listener.exitPrintFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintFunctionCall" ):
                return visitor.visitPrintFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = LinguisParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                localctx = LinguisParser.IdentifierFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(LinguisParser.Identifier)
                self.state = 57
                self.match(LinguisParser.OParen)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132027579957310) != 0):
                    self.state = 58
                    self.exprList()


                self.state = 61
                self.match(LinguisParser.CParen)
                pass
            elif token in [1]:
                localctx = LinguisParser.PrintlnFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(LinguisParser.Println)
                self.state = 63
                self.match(LinguisParser.OParen)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(LinguisParser.CParen)
                pass
            elif token in [2]:
                localctx = LinguisParser.PrintFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(LinguisParser.Print)
                self.state = 68
                self.match(LinguisParser.OParen)
                self.state = 69
                self.expression(0)
                self.state = 70
                self.match(LinguisParser.CParen)
                pass
            elif token in [4]:
                localctx = LinguisParser.AssertFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(LinguisParser.Assert)
                self.state = 73
                self.match(LinguisParser.OParen)
                self.state = 74
                self.expression(0)
                self.state = 75
                self.match(LinguisParser.CParen)
                pass
            elif token in [5]:
                localctx = LinguisParser.SizeFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(LinguisParser.Size)
                self.state = 78
                self.match(LinguisParser.OParen)
                self.state = 79
                self.expression(0)
                self.state = 80
                self.match(LinguisParser.CParen)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStat(self):
            return self.getTypedRuleContext(LinguisParser.IfStatContext,0)


        def End(self):
            return self.getToken(LinguisParser.End, 0)

        def elseIfStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ElseIfStatContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ElseIfStatContext,i)


        def elseStat(self):
            return self.getTypedRuleContext(LinguisParser.ElseStatContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = LinguisParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.ifStat()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 85
                    self.elseIfStat() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 91
                self.elseStat()


            self.state = 94
            self.match(LinguisParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(LinguisParser.If, 0)

        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(LinguisParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = LinguisParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(LinguisParser.If)
            self.state = 97
            self.expression(0)
            self.state = 98
            self.match(LinguisParser.Do)
            self.state = 99
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(LinguisParser.Else, 0)

        def If(self):
            return self.getToken(LinguisParser.If, 0)

        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(LinguisParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_elseIfStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfStat" ):
                listener.enterElseIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfStat" ):
                listener.exitElseIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStat" ):
                return visitor.visitElseIfStat(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStat(self):

        localctx = LinguisParser.ElseIfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseIfStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(LinguisParser.Else)
            self.state = 102
            self.match(LinguisParser.If)
            self.state = 103
            self.expression(0)
            self.state = 104
            self.match(LinguisParser.Do)
            self.state = 105
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(LinguisParser.Else, 0)

        def Do(self):
            return self.getToken(LinguisParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_elseStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStat" ):
                listener.enterElseStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStat" ):
                listener.exitElseStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStat" ):
                return visitor.visitElseStat(self)
            else:
                return visitor.visitChildren(self)




    def elseStat(self):

        localctx = LinguisParser.ElseStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(LinguisParser.Else)
            self.state = 108
            self.match(LinguisParser.Do)
            self.state = 109
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Def(self):
            return self.getToken(LinguisParser.Def, 0)

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)

        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def End(self):
            return self.getToken(LinguisParser.End, 0)

        def idList(self):
            return self.getTypedRuleContext(LinguisParser.IdListContext,0)


        def getRuleIndex(self):
            return LinguisParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = LinguisParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(LinguisParser.Def)
            self.state = 112
            self.match(LinguisParser.Identifier)
            self.state = 113
            self.match(LinguisParser.OParen)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 114
                self.idList()


            self.state = 117
            self.match(LinguisParser.CParen)
            self.state = 118
            self.block()
            self.state = 119
            self.match(LinguisParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For(self):
            return self.getToken(LinguisParser.For, 0)

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)

        def Assign(self):
            return self.getToken(LinguisParser.Assign, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)


        def To(self):
            return self.getToken(LinguisParser.To, 0)

        def Do(self):
            return self.getToken(LinguisParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def End(self):
            return self.getToken(LinguisParser.End, 0)

        def getRuleIndex(self):
            return LinguisParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = LinguisParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(LinguisParser.For)
            self.state = 122
            self.match(LinguisParser.Identifier)
            self.state = 123
            self.match(LinguisParser.Assign)
            self.state = 124
            self.expression(0)
            self.state = 125
            self.match(LinguisParser.To)
            self.state = 126
            self.expression(0)
            self.state = 127
            self.match(LinguisParser.Do)
            self.state = 128
            self.block()
            self.state = 129
            self.match(LinguisParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(LinguisParser.While, 0)

        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def Do(self):
            return self.getToken(LinguisParser.Do, 0)

        def block(self):
            return self.getTypedRuleContext(LinguisParser.BlockContext,0)


        def End(self):
            return self.getToken(LinguisParser.End, 0)

        def getRuleIndex(self):
            return LinguisParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = LinguisParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LinguisParser.While)
            self.state = 132
            self.expression(0)
            self.state = 133
            self.match(LinguisParser.Do)
            self.state = 134
            self.block()
            self.state = 135
            self.match(LinguisParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(LinguisParser.Identifier)
            else:
                return self.getToken(LinguisParser.Identifier, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(LinguisParser.Comma)
            else:
                return self.getToken(LinguisParser.Comma, i)

        def getRuleIndex(self):
            return LinguisParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = LinguisParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(LinguisParser.Identifier)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 138
                self.match(LinguisParser.Comma)
                self.state = 139
                self.match(LinguisParser.Identifier)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(LinguisParser.Comma)
            else:
                return self.getToken(LinguisParser.Comma, i)

        def getRuleIndex(self):
            return LinguisParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = LinguisParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expression(0)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 146
                self.match(LinguisParser.Comma)
                self.state = 147
                self.expression(0)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LinguisParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BoolExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Bool(self):
            return self.getToken(LinguisParser.Bool, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)


    class SubscriptExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)
        def OBracket(self):
            return self.getToken(LinguisParser.OBracket, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CBracket(self):
            return self.getToken(LinguisParser.CBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriptExpression" ):
                listener.enterSubscriptExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriptExpression" ):
                listener.exitSubscriptExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscriptExpression" ):
                return visitor.visitSubscriptExpression(self)
            else:
                return visitor.visitChildren(self)


    class NumberExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(LinguisParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpression" ):
                listener.enterNumberExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpression" ):
                listener.exitNumberExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpression" ):
                return visitor.visitNumberExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(LinguisParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Excl(self):
            return self.getToken(LinguisParser.Excl, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class OrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def Or(self):
            return self.getToken(LinguisParser.Or, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Subtract(self):
            return self.getToken(LinguisParser.Subtract, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpression" ):
                return visitor.visitUnaryMinusExpression(self)
            else:
                return visitor.visitChildren(self)


    class PowerExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.base = None # ExpressionContext
            self.expo = None # ExpressionContext
            self.copyFrom(ctx)

        def Pow(self):
            return self.getToken(LinguisParser.Pow, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpression" ):
                return visitor.visitPowerExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def Equals(self):
            return self.getToken(LinguisParser.Equals, 0)
        def NEquals(self):
            return self.getToken(LinguisParser.NEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpression" ):
                listener.enterEqExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpression" ):
                listener.exitEqExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpression" ):
                return visitor.visitEqExpression(self)
            else:
                return visitor.visitChildren(self)


    class AndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def And(self):
            return self.getToken(LinguisParser.And, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class InExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def In(self):
            return self.getToken(LinguisParser.In, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInExpression" ):
                return visitor.visitInExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def String(self):
            return self.getToken(LinguisParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpression" ):
                listener.enterStringExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpression" ):
                listener.exitStringExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def expression(self):
            return self.getTypedRuleContext(LinguisParser.ExpressionContext,0)

        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionExpression" ):
                listener.enterExpressionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionExpression" ):
                listener.exitExpressionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionExpression" ):
                return visitor.visitExpressionExpression(self)
            else:
                return visitor.visitChildren(self)


    class AddExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def Add(self):
            return self.getToken(LinguisParser.Add, 0)
        def Subtract(self):
            return self.getToken(LinguisParser.Subtract, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpression" ):
                listener.enterAddExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpression" ):
                listener.exitAddExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpression" ):
                return visitor.visitAddExpression(self)
            else:
                return visitor.visitChildren(self)


    class CompExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def GTEquals(self):
            return self.getToken(LinguisParser.GTEquals, 0)
        def LTEquals(self):
            return self.getToken(LinguisParser.LTEquals, 0)
        def GT(self):
            return self.getToken(LinguisParser.GT, 0)
        def LT(self):
            return self.getToken(LinguisParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompExpression" ):
                listener.enterCompExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompExpression" ):
                listener.exitCompExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompExpression" ):
                return visitor.visitCompExpression(self)
            else:
                return visitor.visitChildren(self)


    class NullExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Null(self):
            return self.getToken(LinguisParser.Null, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullExpression" ):
                listener.enterNullExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullExpression" ):
                listener.exitNullExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullExpression" ):
                return visitor.visitNullExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(LinguisParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguisParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LinguisParser.ExpressionContext,i)

        def Multiply(self):
            return self.getToken(LinguisParser.Multiply, 0)
        def Divide(self):
            return self.getToken(LinguisParser.Divide, 0)
        def Modulus(self):
            return self.getToken(LinguisParser.Modulus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpression" ):
                listener.enterMultExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpression" ):
                listener.exitMultExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultExpression" ):
                return visitor.visitMultExpression(self)
            else:
                return visitor.visitChildren(self)


    class ListExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBracket(self):
            return self.getToken(LinguisParser.OBracket, 0)
        def CBracket(self):
            return self.getToken(LinguisParser.CBracket, 0)
        def exprList(self):
            return self.getTypedRuleContext(LinguisParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpression" ):
                listener.enterListExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpression" ):
                listener.exitListExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpression" ):
                return visitor.visitListExpression(self)
            else:
                return visitor.visitChildren(self)


    class InputExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguisParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Input(self):
            return self.getToken(LinguisParser.Input, 0)
        def OParen(self):
            return self.getToken(LinguisParser.OParen, 0)
        def CParen(self):
            return self.getToken(LinguisParser.CParen, 0)
        def String(self):
            return self.getToken(LinguisParser.String, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputExpression" ):
                listener.enterInputExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputExpression" ):
                listener.exitInputExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputExpression" ):
                return visitor.visitInputExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LinguisParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = LinguisParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 154
                self.match(LinguisParser.Subtract)
                self.state = 155
                self.expression(20)
                pass

            elif la_ == 2:
                localctx = LinguisParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(LinguisParser.Excl)
                self.state = 157
                self.expression(19)
                pass

            elif la_ == 3:
                localctx = LinguisParser.NumberExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(LinguisParser.Number)
                pass

            elif la_ == 4:
                localctx = LinguisParser.BoolExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(LinguisParser.Bool)
                pass

            elif la_ == 5:
                localctx = LinguisParser.NullExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(LinguisParser.Null)
                pass

            elif la_ == 6:
                localctx = LinguisParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.functionCall()
                pass

            elif la_ == 7:
                localctx = LinguisParser.ListExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(LinguisParser.OBracket)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132027579957310) != 0):
                    self.state = 163
                    self.exprList()


                self.state = 166
                self.match(LinguisParser.CBracket)
                pass

            elif la_ == 8:
                localctx = LinguisParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 167
                self.match(LinguisParser.Identifier)
                pass

            elif la_ == 9:
                localctx = LinguisParser.SubscriptExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(LinguisParser.Identifier)
                self.state = 169
                self.match(LinguisParser.OBracket)
                self.state = 170
                self.expression(0)
                self.state = 171
                self.match(LinguisParser.CBracket)
                pass

            elif la_ == 10:
                localctx = LinguisParser.StringExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(LinguisParser.String)
                pass

            elif la_ == 11:
                localctx = LinguisParser.ExpressionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.match(LinguisParser.OParen)
                self.state = 175
                self.expression(0)
                self.state = 176
                self.match(LinguisParser.CParen)
                pass

            elif la_ == 12:
                localctx = LinguisParser.InputExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(LinguisParser.Input)
                self.state = 179
                self.match(LinguisParser.OParen)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 180
                    self.match(LinguisParser.String)


                self.state = 183
                self.match(LinguisParser.CParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = LinguisParser.PowerExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 187
                        self.match(LinguisParser.Pow)
                        self.state = 188
                        localctx.expo = self.expression(18)
                        pass

                    elif la_ == 2:
                        localctx = LinguisParser.MultExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 190
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        localctx.right = self.expression(18)
                        pass

                    elif la_ == 3:
                        localctx = LinguisParser.AddExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 193
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        localctx.right = self.expression(17)
                        pass

                    elif la_ == 4:
                        localctx = LinguisParser.CompExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 196
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 106954752) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 197
                        localctx.right = self.expression(16)
                        pass

                    elif la_ == 5:
                        localctx = LinguisParser.EqExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 199
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        localctx.right = self.expression(15)
                        pass

                    elif la_ == 6:
                        localctx = LinguisParser.AndExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 202
                        self.match(LinguisParser.And)
                        self.state = 203
                        self.expression(14)
                        pass

                    elif la_ == 7:
                        localctx = LinguisParser.OrExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 204
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 205
                        self.match(LinguisParser.Or)
                        self.state = 206
                        self.expression(13)
                        pass

                    elif la_ == 8:
                        localctx = LinguisParser.InExpressionContext(self, LinguisParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 207
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 208
                        self.match(LinguisParser.In)
                        self.state = 209
                        self.expression(12)
                        pass

             
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         




