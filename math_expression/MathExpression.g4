
grammar MathExpression;

expression: math_expression EOF;
math_expression: maybe_multiply_expression (('+' | '-') maybe_multiply_expression)*;
maybe_multiply_expression: maybe_negative_value ('*' maybe_negative_value)*;
maybe_negative_value: '-'? value;
value: (Literal | Identifier | '(' math_expression ')');


Literal: Int | Float;
Int: '0' | ([1-9] [0-9]*);
Float: Int '.' [0-9]+;
Identifier: ([a-zA-Z] | '_' )+;
Whitespace: [ \t\r\n]+ -> skip;
