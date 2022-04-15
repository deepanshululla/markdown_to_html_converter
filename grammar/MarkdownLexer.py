# Generated from ./grammar/Markdown.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n=\n\n\3\13\3\13\3\f\3\f")
        buf.write("\3\f\6\fD\n\f\r\f\16\fE\3\r\3\r\3\r\3\r\3\16\6\16M\n\16")
        buf.write("\r\16\16\16N\3\17\3\17\3\17\3\17\5\17U\n\17\3\20\3\20")
        buf.write("\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\2\37\2\3\2\b\6\2))\61\61==aa\5\2")
        buf.write("$$\60\60AA\5\2\62;C\\c|\4\2\13\13\"\"\4\2\f\f\17\17\3")
        buf.write("\2\62;\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2")
        buf.write("\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2\2\21\60\3\2\2\2")
        buf.write("\23<\3\2\2\2\25>\3\2\2\2\27C\3\2\2\2\31G\3\2\2\2\33L\3")
        buf.write("\2\2\2\35T\3\2\2\2\37V\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2#")
        buf.write("$\7+\2\2$\6\3\2\2\2%&\7]\2\2&\b\3\2\2\2\'(\7_\2\2(\n\3")
        buf.write("\2\2\2)*\7%\2\2*\f\3\2\2\2+,\7,\2\2,\16\3\2\2\2-.\7,\2")
        buf.write("\2./\7,\2\2/\20\3\2\2\2\60\61\7,\2\2\61\62\7,\2\2\62\63")
        buf.write("\7,\2\2\63\22\3\2\2\2\64=\t\2\2\2\65\66\7?\2\2\66=\7$")
        buf.write("\2\2\67=\t\3\2\289\7<\2\29:\7\61\2\2:=\7\61\2\2;=\7.\2")
        buf.write("\2<\64\3\2\2\2<\65\3\2\2\2<\67\3\2\2\2<8\3\2\2\2<;\3\2")
        buf.write("\2\2=\24\3\2\2\2>?\7\"\2\2?\26\3\2\2\2@D\t\4\2\2AD\5\23")
        buf.write("\n\2BD\5\25\13\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2DE\3\2\2")
        buf.write("\2EC\3\2\2\2EF\3\2\2\2F\30\3\2\2\2GH\t\5\2\2HI\3\2\2\2")
        buf.write("IJ\b\r\2\2J\32\3\2\2\2KM\t\6\2\2LK\3\2\2\2MN\3\2\2\2N")
        buf.write("L\3\2\2\2NO\3\2\2\2O\34\3\2\2\2PQ\7^\2\2QU\7$\2\2RS\7")
        buf.write("^\2\2SU\7^\2\2TP\3\2\2\2TR\3\2\2\2U\36\3\2\2\2VW\t\7\2")
        buf.write("\2W \3\2\2\2\b\2<CENT\3\b\2\2")
        return buf.getvalue()


class MarkdownLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    SYMBOLS = 9
    SPACE = 10
    TEXT = 11
    WS = 12
    NEWLINE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'#'", "'*'", "'**'", "'***'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "SYMBOLS", "SPACE", "TEXT", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "SYMBOLS", "SPACE", "TEXT", "WS", "NEWLINE", "ESC", 
                  "DIGIT" ]

    grammarFileName = "Markdown.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


