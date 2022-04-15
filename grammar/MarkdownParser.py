# Generated from ./grammar/Markdown.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3)\n\3\3\4\3\4\3\5\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\3\6\3\6\6\6\67\n\6\r\6\16\68\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\6\tE\n\t\r\t\16\tF\3\n\3\n\6\nK\n")
        buf.write("\n\r\n\16\nL\3\13\6\13P\n\13\r\13\16\13Q\3\13\3\13\7\13")
        buf.write("V\n\13\f\13\16\13Y\13\13\3\f\3\f\6\f]\n\f\r\f\16\f^\3")
        buf.write("\f\3\f\3\r\3\r\6\re\n\r\r\r\16\rf\3\r\3\r\3\16\3\16\6")
        buf.write("\16m\n\16\r\16\16\16n\3\16\3\16\3\16\3\37\2\17\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\2\3\3\2\f\r\2x\2\37\3\2\2\2")
        buf.write("\4(\3\2\2\2\6*\3\2\2\2\b,\3\2\2\2\n\64\3\2\2\2\f<\3\2")
        buf.write("\2\2\16?\3\2\2\2\20D\3\2\2\2\22J\3\2\2\2\24O\3\2\2\2\26")
        buf.write("Z\3\2\2\2\30b\3\2\2\2\32j\3\2\2\2\34\36\5\4\3\2\35\34")
        buf.write("\3\2\2\2\36!\3\2\2\2\37 \3\2\2\2\37\35\3\2\2\2 \3\3\2")
        buf.write("\2\2!\37\3\2\2\2\")\5\24\13\2#)\5\26\f\2$)\5\30\r\2%)")
        buf.write("\5\32\16\2&)\5\20\t\2\')\5\6\4\2(\"\3\2\2\2(#\3\2\2\2")
        buf.write("($\3\2\2\2(%\3\2\2\2(&\3\2\2\2(\'\3\2\2\2)\5\3\2\2\2*")
        buf.write("+\7\17\2\2+\7\3\2\2\2,.\7\3\2\2-/\7\r\2\2.-\3\2\2\2/\60")
        buf.write("\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63")
        buf.write("\7\4\2\2\63\t\3\2\2\2\64\66\7\5\2\2\65\67\7\r\2\2\66\65")
        buf.write("\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:")
        buf.write(";\7\6\2\2;\13\3\2\2\2<=\5\n\6\2=>\5\b\5\2>\r\3\2\2\2?")
        buf.write("@\t\2\2\2@\17\3\2\2\2AE\5\f\7\2BE\5\16\b\2CE\7\17\2\2")
        buf.write("DA\3\2\2\2DB\3\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3")
        buf.write("\2\2\2G\21\3\2\2\2HK\5\20\t\2IK\7\17\2\2JH\3\2\2\2JI\3")
        buf.write("\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\23\3\2\2\2NP\7\7")
        buf.write("\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2RW\3\2\2\2")
        buf.write("SV\5\16\b\2TV\5\f\7\2US\3\2\2\2UT\3\2\2\2VY\3\2\2\2WU")
        buf.write("\3\2\2\2WX\3\2\2\2X\25\3\2\2\2YW\3\2\2\2Z\\\7\b\2\2[]")
        buf.write("\5\16\b\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_`")
        buf.write("\3\2\2\2`a\7\b\2\2a\27\3\2\2\2bd\7\t\2\2ce\5\16\b\2dc")
        buf.write("\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\7\t")
        buf.write("\2\2i\31\3\2\2\2jl\7\n\2\2km\5\16\b\2lk\3\2\2\2mn\3\2")
        buf.write("\2\2nl\3\2\2\2no\3\2\2\2op\3\2\2\2pq\7\n\2\2q\33\3\2\2")
        buf.write("\2\20\37(\608DFJLQUW^fn")
        return buf.getvalue()


class MarkdownParser ( Parser ):

    grammarFileName = "Markdown.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'#'", "'*'", 
                     "'**'", "'***'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SYMBOLS", "SPACE", "TEXT", "WS", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_newline = 2
    RULE_url = 3
    RULE_linked_text = 4
    RULE_link = 5
    RULE_plaintext = 6
    RULE_para = 7
    RULE_text = 8
    RULE_heading = 9
    RULE_italic = 10
    RULE_bold = 11
    RULE_bolditalic = 12

    ruleNames =  [ "program", "statement", "newline", "url", "linked_text", 
                   "link", "plaintext", "para", "text", "heading", "italic", 
                   "bold", "bolditalic" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    SYMBOLS=9
    SPACE=10
    TEXT=11
    WS=12
    NEWLINE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.StatementContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.StatementContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MarkdownParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 26
                    self.statement() 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def heading(self):
            return self.getTypedRuleContext(MarkdownParser.HeadingContext,0)


        def italic(self):
            return self.getTypedRuleContext(MarkdownParser.ItalicContext,0)


        def bold(self):
            return self.getTypedRuleContext(MarkdownParser.BoldContext,0)


        def bolditalic(self):
            return self.getTypedRuleContext(MarkdownParser.BolditalicContext,0)


        def para(self):
            return self.getTypedRuleContext(MarkdownParser.ParaContext,0)


        def newline(self):
            return self.getTypedRuleContext(MarkdownParser.NewlineContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MarkdownParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.heading()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.italic()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.bold()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.bolditalic()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                self.para()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 37
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MarkdownParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = MarkdownParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MarkdownParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UrlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.TEXT)
            else:
                return self.getToken(MarkdownParser.TEXT, i)

        def getRuleIndex(self):
            return MarkdownParser.RULE_url

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = MarkdownParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(MarkdownParser.T__0)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.match(MarkdownParser.TEXT)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MarkdownParser.TEXT):
                    break

            self.state = 48
            self.match(MarkdownParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Linked_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.TEXT)
            else:
                return self.getToken(MarkdownParser.TEXT, i)

        def getRuleIndex(self):
            return MarkdownParser.RULE_linked_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinked_text" ):
                return visitor.visitLinked_text(self)
            else:
                return visitor.visitChildren(self)




    def linked_text(self):

        localctx = MarkdownParser.Linked_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_linked_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MarkdownParser.T__2)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.match(MarkdownParser.TEXT)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MarkdownParser.TEXT):
                    break

            self.state = 56
            self.match(MarkdownParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LinkContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def linked_text(self):
            return self.getTypedRuleContext(MarkdownParser.Linked_textContext,0)


        def url(self):
            return self.getTypedRuleContext(MarkdownParser.UrlContext,0)


        def getRuleIndex(self):
            return MarkdownParser.RULE_link

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = MarkdownParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.linked_text()
            self.state = 59
            self.url()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlaintextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(MarkdownParser.TEXT, 0)

        def SPACE(self):
            return self.getToken(MarkdownParser.SPACE, 0)

        def getRuleIndex(self):
            return MarkdownParser.RULE_plaintext

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlaintext" ):
                return visitor.visitPlaintext(self)
            else:
                return visitor.visitChildren(self)




    def plaintext(self):

        localctx = MarkdownParser.PlaintextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_plaintext)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==MarkdownParser.SPACE or _la==MarkdownParser.TEXT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.LinkContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.LinkContext,i)


        def plaintext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.PlaintextContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.PlaintextContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.NEWLINE)
            else:
                return self.getToken(MarkdownParser.NEWLINE, i)

        def getRuleIndex(self):
            return MarkdownParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MarkdownParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 66
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MarkdownParser.T__2]:
                        self.state = 63
                        self.link()
                        pass
                    elif token in [MarkdownParser.SPACE, MarkdownParser.TEXT]:
                        self.state = 64
                        self.plaintext()
                        pass
                    elif token in [MarkdownParser.NEWLINE]:
                        self.state = 65
                        self.match(MarkdownParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 68 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.ParaContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.ParaContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MarkdownParser.NEWLINE)
            else:
                return self.getToken(MarkdownParser.NEWLINE, i)

        def getRuleIndex(self):
            return MarkdownParser.RULE_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = MarkdownParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 70
                    self.para()
                    pass

                elif la_ == 2:
                    self.state = 71
                    self.match(MarkdownParser.NEWLINE)
                    pass


                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MarkdownParser.T__2) | (1 << MarkdownParser.SPACE) | (1 << MarkdownParser.TEXT) | (1 << MarkdownParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeadingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plaintext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.PlaintextContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.PlaintextContext,i)


        def link(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.LinkContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.LinkContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_heading

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeading" ):
                return visitor.visitHeading(self)
            else:
                return visitor.visitChildren(self)




    def heading(self):

        localctx = MarkdownParser.HeadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_heading)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 76
                    self.match(MarkdownParser.T__4)

                else:
                    raise NoViableAltException(self)
                self.state = 79 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MarkdownParser.SPACE, MarkdownParser.TEXT]:
                        self.state = 81
                        self.plaintext()
                        pass
                    elif token in [MarkdownParser.T__2]:
                        self.state = 82
                        self.link()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItalicContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plaintext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.PlaintextContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.PlaintextContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_italic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItalic" ):
                return visitor.visitItalic(self)
            else:
                return visitor.visitChildren(self)




    def italic(self):

        localctx = MarkdownParser.ItalicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_italic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MarkdownParser.T__5)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.plaintext()
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MarkdownParser.SPACE or _la==MarkdownParser.TEXT):
                    break

            self.state = 94
            self.match(MarkdownParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plaintext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.PlaintextContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.PlaintextContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_bold

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBold" ):
                return visitor.visitBold(self)
            else:
                return visitor.visitChildren(self)




    def bold(self):

        localctx = MarkdownParser.BoldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bold)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MarkdownParser.T__6)
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.plaintext()
                self.state = 100 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MarkdownParser.SPACE or _la==MarkdownParser.TEXT):
                    break

            self.state = 102
            self.match(MarkdownParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BolditalicContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plaintext(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MarkdownParser.PlaintextContext)
            else:
                return self.getTypedRuleContext(MarkdownParser.PlaintextContext,i)


        def getRuleIndex(self):
            return MarkdownParser.RULE_bolditalic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBolditalic" ):
                return visitor.visitBolditalic(self)
            else:
                return visitor.visitChildren(self)




    def bolditalic(self):

        localctx = MarkdownParser.BolditalicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bolditalic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MarkdownParser.T__7)
            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.plaintext()
                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MarkdownParser.SPACE or _la==MarkdownParser.TEXT):
                    break

            self.state = 110
            self.match(MarkdownParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





