lexer grammar LinguisFRFRLexer;

Println  : 'imprimerdb';
Print    : 'imprimer';
Input    : 'saisir';
Assert   : 'affirmer';
Size     : 'taille';
Def      : 'définir';
If       : 'si';
Else     : 'autre';
Return   : 'retour';
For      : 'pour';
While    : 'alors que';
To       : 'to';
Do       : 'à';
End      : 'fin';
In       : 'dans';
Null     : 'nulle';

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
 : 'vraie' 
 | 'faux'
 ;

Number
 : Int ( '.' Digit* )?
 ;

// Include more Unicode characters?
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
