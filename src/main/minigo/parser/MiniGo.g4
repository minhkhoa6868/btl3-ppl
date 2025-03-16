// 2252365

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
last_tk = None

def emit(self):
    tk = self.type
    if tk not in {self.WS, self.NL}:
        self.last_tk = tk

    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

def handle_newline(self):
    # check next token
    next_tk = self._input.LA(1)

    while next_tk in {ord(' '), ord('\t')}:
        # move to next char
        self._input.consume()
        # check again
        next_tk = self._input.LA(1)

    if self.last_tk in {self.ID, self.INT_LITERALS, self.FLOAT_LITERALS, self.STRING_LITERALS,
                        self.CONTINUE, self.BREAK, self.RIGHT_BRACE, self.RIGHT_SQUARE_BRACKET,
                        self.RETURN_WORD, self.PRIMITIVE_TYPE, self.BOOLEAN_LITERALS}:
        if next_tk in {ord('\n'), ord('\r')} or next_tk not in {ord(';'), ord('{')}:
            self.type = self.SEMICOLON
            self.text = ";"
            return self.emit()

    if self.last_tk == self.RIGHT_PARENTHESES:
        if next_tk == self.NL:
            self._input.consume()
            next_tk = self._input.LA(1)

        while next_tk == self.WS:
            self._input.consume()
            next_tk = self._input.LA(1)

        if next_tk in {ord('+'), ord('-'), ord('*'), ord('/'), ord('%'), ord('='), ord('['), ord('(')}:
            return self.skip()

        if next_tk not in {ord(';'), ord('{')}:
            self.type = self.SEMICOLON
            self.text = ";"
            return self.emit()
    
    return self.skip()
}

options{
	language=Python3;
}

PRIMITIVE_TYPE: 'int' | 'float' | 'string' | 'boolean'; 
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN_WORD: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';

DOT: '.';
DIFFERENT: '!';
SEMICOLON: ';';

LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
LEFT_PARENTHESES: '(';
RIGHT_PARENTHESES: ')';
COLONS: ':';

// Operators
EQUAL: '=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
AND: '&&';
OR: '||';

PLUS_EQUAL: '+=';
MINUS_EQUAL: '-=';
MULTIPLY_EQUAL: '*=';
DIVIDE_EQUAL: '/=';
MODULO_EQUAL: '%=';
COLONS_EQUAL: ':=';
SMALLER: '<';
SMALLER_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';
DOUBLE_EQUAL: '==';
DIFFERENT_EQUAL: '!=';

COMMENT: '//';
TAB: '\t';
RETURN: '\r';
BACKSLASH: '\\';
UNDERSCORE: '_';

// int
fragment Digit: [0-9];
INT_LITERALS: '-'? ( '0' | [1-9]Digit* | '0b' [01]+ | '0B' [01]+ | '0o' [0-7]+ | '0O' [0-7]+ | '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+);

// float
fragment Exponent: [eE] [+-]? Digit+;
FLOAT_LITERALS: '-'? Digit+ '.' (Digit+)? Exponent?; 

// string
fragment Accept_char: '\\' [ntrfb"'\\]; 
STRING_LITERALS: '"' (Accept_char | ~["\\\n\r\b\f])* '"';

// boolean
BOOLEAN_LITERALS: ('true' | 'false');

// nil
NIL: 'nil';

// id
ID: [a-zA-Z_][a-zA-Z_0-9]*;

expression_string: expression_string relational plus_string |
                   plus_string
                   ;
plus_string: plus_string '+' term_plus | term_plus;
term_plus: STRING_LITERALS | ID | access_field | expression_array | '(' expression_string ')' ;

expression_float: expression_float relational add_float |
                  add_float
                  ;
add_float: add_float ('+' | '-') mul_float | 
           mul_float
           ;
mul_float: mul_float ('*' | '/') unary_float | 
           unary_float 
           ;
unary_float: '-' unary_float | term_float ;
term_float: ID | FLOAT_LITERALS | INT_LITERALS | access_field | expression_array | '(' expression_float ')' ;

expression_int: expression_int relational add_int |
                add_int
                ;
add_int: add_int ('+' | '-') mul_int | 
         mul_int 
         ;
mul_int: mul_int ('*' | '/' | '%') unary_int | 
         unary_int 
         ;
unary_int: '-' unary_int | term_int ;
term_int: ID | INT_LITERALS | access_field | expression_array | '(' expression_int ')' ;

expression_boolean: expression_boolean OR and_boolean |
                    and_boolean
                    ;
and_boolean: and_boolean AND compare_boolean | 
             compare_boolean 
             ;
compare_boolean: compare_boolean ('==' | '!=') unary_boolean | 
                 unary_boolean
                 ;
unary_boolean: '!' unary_boolean | term_boolean ;
term_boolean: BOOLEAN_LITERALS | expression_int | expression_float | expression_string | '(' expression_boolean ')' ;

// array declaration
expression_array: arrays_type '{' array_instance? '}';
array_size: expression_int;
arrays_type: ('[' array_size ']')+ (PRIMITIVE_TYPE | ID);
array_instance: array_value (',' array_value)*;
array_value: expression_boolean |
             expression_int | 
             expression_float |
             expression_string |
             struct_value |
             '{' array_value (',' array_value)* '}' |
             '{' '}'
             ;
array_idx: expression_boolean |
           expression_int | 
           expression_float |
           expression_string
           ;
array_access_field: arr_name ('[' array_idx ']')+ ;
arr_name: ID | callfuncdecl | INT_LITERALS | FLOAT_LITERALS | STRING_LITERALS | BOOLEAN_LITERALS | '(' expression_int ')' | '(' expression_float ')' | '(' expression_string ')' | '(' expression_boolean ')';

// access field
access_field: access_field '.' field |     
              access_field '.' callfuncdecl |
              callfuncdecl |
              field ;
field: ID | array_access_field | '(' expression_int ')' | '(' expression_float ')' | '(' expression_string ')' | '(' expression_boolean ')' ;

// struct instance declaration
struct_value: ID '{' field_value? '}';
field_value: ID ':' value_assign (',' ID ':' value_assign)*;

relational: SMALLER | SMALLER_EQUAL | GREATER | GREATER_EQUAL | DOUBLE_EQUAL | DIFFERENT_EQUAL;
other_operations:  PLUS_EQUAL | MINUS_EQUAL | MULTIPLY_EQUAL | DIVIDE_EQUAL | MODULO_EQUAL;

program  : decl+ EOF ;

decl: vardecl | constdecl | shortvardecl | funcdecl |  structdecl | interfacedecl;

funcdecl: 'func' receiver? ID LEFT_PARENTHESES funcParams? RIGHT_PARENTHESES funcType? LEFT_BRACE block+ RIGHT_BRACE SEMICOLON? ;
funcParams: funcParam ',' funcParams | funcParam ;
funcParam: funcListName funcType ;
funcListName: ID ',' funcListName | ID ;
funcType: PRIMITIVE_TYPE | ID | arrays_type ;
// func block
block: vardecl | constdecl | shortvardecl | returndecl | ifelsedecl | forloopdecl | access_field | funcdecl;
receiver: '(' ID ID ')';

structdecl: 'type' ID 'struct' LEFT_BRACE struct_field+ RIGHT_BRACE (SEMICOLON | NL) ;
// struct declaration
struct_field: ID struct_fieldType (SEMICOLON | NL);
struct_fieldType: PRIMITIVE_TYPE | ID | arrays_type ;

interfacedecl: 'type' ID 'interface' '{' interface_field+ '}' (SEMICOLON | NL);
// interface declaration
interface_field: ID LEFT_PARENTHESES interfaceParams? RIGHT_PARENTHESES interfaceType? (SEMICOLON | NL) ;
interfaceParams: interfaceParam ',' interfaceParams | interfaceParam ;
interfaceParam: interfaceListName interfaceType ;
interfaceListName: ID ',' interfaceListName | ID ;
interfaceType: PRIMITIVE_TYPE | ID | arrays_type ;

vardecl: 'var' ID varType ('=' value_assign)? (SEMICOLON | NL) | 
         'var' ID '=' value_assign (SEMICOLON | NL) ;
varType: PRIMITIVE_TYPE | arrays_type | ID ;

constdecl: 'const' ID '=' value_assign (SEMICOLON | NL) ;

shortvardecl: lhs assign_operators value_assign (SEMICOLON | NL);
lhs: ID | access_field;
assign_operators: other_operations | COLONS_EQUAL;

returndecl: 'return' value_assign (SEMICOLON | NL) |
            'return' (SEMICOLON | NL)
            ;

callfuncdecl: ID '(' argu_list ')' SEMICOLON?|
              ID '(' ')' SEMICOLON?
              ;
// parameter
argu_list: value_assign (',' value_assign)* ;
value_assign: struct_value |
              NIL | 
              expression_boolean |
              expression_array | 
              expression_int | 
              expression_float |
              expression_string |
              '(' value_assign ')'
              ;

breakdecl: BREAK (SEMICOLON | NL) ;

continuedecl: CONTINUE (SEMICOLON | NL) ;

ifelsedecl: 'if' '(' expression_boolean ')' '{' block+ '}' SEMICOLON? elifdecls? elsedecl? ;

elifdecls: elifdecl elifdecls | elifdecl ;
elifdecl: 'else' 'if' '(' expression_boolean ')' '{' block+ '}' SEMICOLON? ;

elsedecl: 'else' '{' block+ '}' (SEMICOLON | NL) ;

ifelsedecl_inside_loop: 'if' '(' expression_boolean ')' '{' block_inside_loop+ '}' SEMICOLON? elifdecls_inside_loop? elsedecl_inside_loop? ;

elifdecls_inside_loop: elifdecl_inside_loop elifdecls_inside_loop | elifdecl_inside_loop ;
elifdecl_inside_loop: 'else' 'if' '(' expression_boolean ')' '{' block_inside_loop+ '}' SEMICOLON? ;

elsedecl_inside_loop: 'else' '{' block_inside_loop+ '}' (SEMICOLON | NL) ;

forloopdecl: 'for' condition '{' block_inside_loop+ '}' (SEMICOLON | NL) |
             'for' initialization ';' condition ';' update '{' block_inside_loop+ '}' (SEMICOLON | NL) |
             'for' for_access_value ',' for_access_value COLONS_EQUAL RANGE for_arr '{' block_inside_loop+ '}' (SEMICOLON | NL)
             ;
for_access_value: ID | UNDERSCORE;
for_arr: ID | expression_array | access_field ;
// for loop block
block_inside_loop: vardecl | constdecl | shortvardecl | returndecl | ifelsedecl_inside_loop | breakdecl | continuedecl | forloopdecl | access_field;
initialization: ID COLONS_EQUAL value_assign ;
condition: expression_boolean ;
update: ID other_operations value_assign ;

SINGLE_COMMENT: COMMENT ~[\r\n]* -> skip; // skip comments

MULTI_COMMENT: '/*' (MULTI_COMMENT | ~[/*]+)* '*/' -> skip; // skip multi line comments

NL: '\n' { self.handle_newline() } ; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

ILLEGAL_ESCAPE : '"' (~["\\\r\n\t] | Accept_char)* '\\' ~[btnfr"'\\];
END_NEWLINE: '"' (~[\r\n\\"] | '\\' [nrft'\\])* '\n' {raise UncloseString(self.text[:-1])} ;
END_RETURN_NEWLINE: '"' (~[\r\n\\"] | '\\' [nrft'\\])* '\r\n' {raise UncloseString(self.text[:-2])} ;
END_EOF: '"' (~[\r\n\\"] | '\\' [nrft'\\])* EOF {raise UncloseString(self.text[:])} ;
UNCLOSE_STRING: END_NEWLINE | END_RETURN_NEWLINE| END_EOF;
ERROR_CHAR: .;