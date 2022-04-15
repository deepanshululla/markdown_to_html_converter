grammar Markdown;

program    :   statement*?;

statement    : heading
            |   italic
            |   bold
            |   bolditalic
            |   para
            |   newline
            ;

newline : NEWLINE;
url: ('('TEXT+')');
linked_text: ('['TEXT+']');
link: (linked_text url);
plaintext: TEXT|SPACE;
para: (link | plaintext| NEWLINE)+;
heading : '#'+ (plaintext|link)*;
italic  :   ('*'plaintext+'*');
bold    :   ('**'plaintext+'**');

bolditalic: ('***' plaintext+ '***');
SYMBOLS: ('\'' | '_'  | '/' | ';' | '="' | '"' | '?' | '.' | '://' | ',');
SPACE: ' ';
TEXT : ([a-zA-Z0-9] | SYMBOLS | SPACE)+;
WS :   [ \t]->skip;

NEWLINE: [\r\n]+;
fragment
ESC: '\\"'|'\\\\';
fragment
DIGIT: [0-9];
