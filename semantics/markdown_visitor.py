from markdown_to_html_converter.grammar.MarkdownParser import MarkdownParser
from markdown_to_html_converter.grammar.MarkdownVisitor import MarkdownVisitor
from markdown_to_html_converter.semantics.code_generator import CodeGenerator


class MarkdownAst(MarkdownVisitor):
    def __init__(self, code_generator: CodeGenerator):
        self.code_gen = code_generator

    def visitProgram(self, ctx: MarkdownParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitStatement(self, ctx: MarkdownParser.StatementContext):
        return super().visitStatement(ctx)

    def visitNewline(self, ctx: MarkdownParser.NewlineContext):
        return super().visitNewline(ctx)

    def visitPlaintext(self, ctx: MarkdownParser.PlaintextContext):
        return ctx.getText().lstrip().rstrip()

    def visitLink(self, ctx: MarkdownParser.LinkContext):
        children = ctx.children
        linked_text = children[0].getText().strip("[]")
        url = children[1].getText().strip("()")
        return f' <a href="{url}">{linked_text}</a>'

    def visitPara(self, ctx: MarkdownParser.ParaContext):
        result = []
        n = len(ctx.children)
        i = 0
        current_text = []
        while i < n:
            child = ctx.children[i]
            text = child.getText()
            if type(child) in (MarkdownParser.PlaintextContext, MarkdownParser.LinkContext):
                current_text.append(self.visit(child))
            elif text == "\n\n" and current_text:
                result.append("".join(current_text))
                current_text = []
            elif text == "\n":
                current_text.append(text)
            i += 1
        for line in result:
            self.code_gen.append("<p>")
            self.code_gen.append(line.strip('\n').strip())
            self.code_gen.append("</p>")
            self.code_gen.append("\n")


    def visitHeading(self, ctx: MarkdownParser.HeadingContext):
        number_of_pounds = [c.getText() for c in ctx.children]
        headerNumber = number_of_pounds.count("#")
        self.code_gen.append("\n")
        self.code_gen.append(f"<h{headerNumber}>")
        for child in ctx.children[headerNumber:]:
            self.code_gen.append(self.visit(child))
        self.code_gen.append(f"</h{headerNumber}>")
        self.code_gen.append("\n")

    def visitItalic(self, ctx: MarkdownParser.ItalicContext):
        self.code_gen.append("<i> ")
        for child in ctx.children:
            self.code_gen.append(self.visit(child))
        self.code_gen.append("</i>")

    def visitBold(self, ctx: MarkdownParser.BoldContext):
        self.code_gen.append("<strong>")
        for child in ctx.children:
            self.code_gen.append(self.visit(child))
        self.code_gen.append("</strong>")

    def visitBolditalic(self, ctx: MarkdownParser.BolditalicContext):
        self.code_gen.append("<strong><i> ")
        for child in ctx.children:
            self.code_gen.append(self.visit(child))
        self.code_gen.append("</i></strong>")
