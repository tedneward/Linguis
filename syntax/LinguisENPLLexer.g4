// Owdyhay, Igpay Atinway Englishway!
lexer grammar LinguisLexer;

Println  : 'intlnpray';
Print    : 'intpray';
Input    : 'inputway';
Assert   : 'assertway';
Size     : 'izesay';
Def      : 'efday';
If       : 'ifway';
Else     : 'elseway';
Return   : 'eturnray';
For      : 'orfay';
While    : 'ilewhay';
To       : 'otay';
Do       : 'oday';
End      : 'endway';
In       : 'inway';
Null     : 'ullnay';

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
 : 'uetray' 
 | 'alsefay'
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
 ;