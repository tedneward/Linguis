parser grammar LinguisParser;

options {
    tokenVocab = LinguisLexer;
}

block
 : ( statement | functionDecl )* ( Return expression ';' )?
 ;

statement
 : assignment ';'
 | functionCall ';'
 | ifStatement
 | forStatement
 | whileStatement
 ;

assignment
 : Identifier '=' expression
 ;

functionCall
 : Identifier '(' exprList? ')' #identifierFunctionCall
 | Println '(' expression ')'   #printlnFunctionCall
 | Print '(' expression ')'     #printFunctionCall
 | Assert '(' expression ')'    #assertFunctionCall
 | Size '(' expression ')'      #sizeFunctionCall
 ;

ifStatement
 : ifStat elseIfStat* elseStat? End
 ;

ifStat
 : If expression Do block
 ;

elseIfStat
 : Else If expression Do block
 ;

elseStat
 : Else Do block
 ;

functionDecl
 : Def Identifier '(' idList? ')' block End
 ;

forStatement
 : For Identifier '=' expression To expression Do block End
 ;

whileStatement
 : While expression Do block End
 ;

idList
 : Identifier ( ',' Identifier )*
 ;

exprList
 : expression ( ',' expression )*
 ;

expression
 : '-' expression                                       #unaryMinusExpression
 | '!' expression                                       #notExpression
 | <assoc=right> base=expression '^' expo=expression               #powerExpression
 | left=expression op=( '*' | '/' | '%' ) right=expression         #multExpression
 | left=expression op=( '+' | '-' ) right=expression               #addExpression
 | left=expression op=( '>=' | '<=' | '>' | '<' ) right=expression #compExpression
 | left=expression op=( '==' | '!=' ) right=expression             #eqExpression
 | expression '&&' expression                           #andExpression
 | expression '||' expression                           #orExpression
 | expression In expression                             #inExpression
 | Number                                               #numberExpression
 | Bool                                                 #boolExpression
 | Null                                                 #nullExpression
 | functionCall                                         #functionCallExpression
 | '[' exprList? ']'                                    #listExpression
 | Identifier                                           #identifierExpression
 | Identifier '[' expression ']'                        #subscriptExpression
 | String                                               #stringExpression
 | '(' expression ')'                                   #expressionExpression
 | Input '(' String? ')'                                #inputExpression
 ;

