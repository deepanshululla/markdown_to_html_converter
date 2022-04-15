# Generated from ./grammar/Markdown.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MarkdownParser import MarkdownParser
else:
    from MarkdownParser import MarkdownParser

# This class defines a complete generic visitor for a parse tree produced by MarkdownParser.

class MarkdownVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MarkdownParser#program.
    def visitProgram(self, ctx:MarkdownParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#statement.
    def visitStatement(self, ctx:MarkdownParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#newline.
    def visitNewline(self, ctx:MarkdownParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#url.
    def visitUrl(self, ctx:MarkdownParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#linked_text.
    def visitLinked_text(self, ctx:MarkdownParser.Linked_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#link.
    def visitLink(self, ctx:MarkdownParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#plaintext.
    def visitPlaintext(self, ctx:MarkdownParser.PlaintextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#para.
    def visitPara(self, ctx:MarkdownParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#text.
    def visitText(self, ctx:MarkdownParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#heading.
    def visitHeading(self, ctx:MarkdownParser.HeadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#italic.
    def visitItalic(self, ctx:MarkdownParser.ItalicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#bold.
    def visitBold(self, ctx:MarkdownParser.BoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MarkdownParser#bolditalic.
    def visitBolditalic(self, ctx:MarkdownParser.BolditalicContext):
        return self.visitChildren(ctx)



del MarkdownParser