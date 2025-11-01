# Linguis high-level syntax and semantics

Linguis is a dynamically-typed, procedural (as opposed to "functional") imperative language that supports a few core types and a few common procedural flow-control constructs.

## Types
Linguis supports boolean, integer, floating-point, string, and list types. The null literal represents no value.

## Variables

Like Python, Linguis variables need not be declared, and are allocated/available upon first use (which is almost always an assignment).

## Operators

### Unary
Integer and floating-point types can be negated via the unary negation (`-`) operator.

Strings and lists cannot be negated.

### Binary
Integer and floating-point types support all the canonical binary mathematical operators (`+`, `-`, `*`, `/`, and `%`), as well as exponential (`^`).

## Flow control

### Decision-making (`if`)

Decision-making requires some kind of "truthy" expression-yielding value.

### Finite iteration (`for`)

Finite iteration is limited to integer counts, a la "for a = 0 to 3 do ... end"; no "iterable objects" like lists as in Python. (We could, I suppose, support "for a = [1,2,3]", meaning a gets an iterator and iterates through it, but that seems tangential to the language goal.)

### Infinite iteration (`while`)

## Functions

Functions are defined by a keyword (`def` in ENUS) followed by an identifier followed by parentheses declaring parameters. The function body is itself a block. The body is indented.

Functions are invoked by using the identifier followed by parentheses, with the necessary parameters listed. 

## Runtime semantics

If a Linguis program violates the semantics described here, it will raise an exception and terminate; no catch-and-resume behavior is supported.

## ANTLR syntax:

```
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
 : Identifier indexes? '=' expression
 ;

functionCall
 : Identifier '(' exprList? ')' #identifierFunctionCall
 | Println '(' expression? ')'  #printlnFunctionCall
 | Print '(' expression ')'     #printFunctionCall
 | Input '(' expression ')'     #inputFunctionCall
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
 | <assoc=right> expression '^' expression              #powerExpression
 | expression op=( '*' | '/' | '%' ) expression         #multExpression
 | expression op=( '+' | '-' ) expression               #addExpression
 | expression op=( '>=' | '<=' | '>' | '<' ) expression #compExpression
 | expression op=( '==' | '!=' ) expression             #eqExpression
 | expression '&&' expression                           #andExpression
 | expression '||' expression                           #orExpression
 | expression In expression                             #inExpression
 | Number                                               #numberExpression
 | Bool                                                 #boolExpression
 | Null                                                 #nullExpression
 | functionCall indexes?                                #functionCallExpression
 | list indexes?                                        #listExpression
 | Identifier indexes?                                  #identifierExpression
 | String indexes?                                      #stringExpression
 | '(' expression ')' indexes?                          #expressionExpression
 | Input '(' String? ')'                                #inputExpression
 ;

list
 : '[' exprList? ']'
 ;

indexes
 : ( '[' expression ']' )+
 ;
```

This, for example, would be the English-lexed syntax. Presumably the operators would remain the same across syntaxes, but why make assumptions? Different alphabets might have a more interesting way to represent a given math/comparison operation.

```
Println  : 'println';
Print    : 'print';
Input    : 'input';
Assert   : 'assert';
Size     : 'size';

Def      : 'def';
If       : 'if';
Else     : 'else';
Return   : 'return';
For      : 'for';
While    : 'while';
To       : 'to';
Do       : 'do';
End      : 'end';
In       : 'in';
Null     : 'null';

Or       : '||';
And      : '&&';
Equals   : '==';
NEquals  : '!=';
GTEquals : '>=';
LTEquals : '<=';
Pow      : '^';
Excl     : '!';
GT       : '>';
LT       : '<';
Add      : '+';
Subtract : '-';
Multiply : '*';
Divide   : '/';
Modulus  : '%';
OBrace   : '{';
CBrace   : '}';
OBracket : '[';
CBracket : ']';
OParen   : '(';
CParen   : ')';
SColon   : ';';
Assign   : '=';
Comma    : ',';
QMark    : '?';
Colon    : ':';

Bool
 : 'true' 
 | 'false'
 ;

Number
 : Int ( '.' Digit* )?
 ;

Identifier
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

String
 : ["] ( ~["\r\n\\] | '\\' ~[\r\n] )* ["]
 | ['] ( ~['\r\n\\] | '\\' ~[\r\n] )* [']
 ;

Comment
 : ( '//' ~[\r\n]* | '/*' .*? '*/' ) -> skip
 ;

Space
 : [ \t\r\n\u000C] -> skip
 ;

fragment Int
 : [1-9] Digit*
 | '0'
 ;
  
fragment Digit 
 : [0-9]
 ;% 
```
