from antlr4 import CommonTokenStream, InputStream

from markdown_to_html_converter.grammar.MarkdownLexer import MarkdownLexer
from markdown_to_html_converter.grammar.MarkdownParser import MarkdownParser
from markdown_to_html_converter.semantics.code_generator import *
from markdown_to_html_converter.semantics.markdown_visitor import MarkdownAst

class MarkdownToHtml:
    def __init__(self, md_file: str):
        self.md_file = md_file

    def parse(self):
        code_gen = CodeGenerator()
        with open(self.md_file) as f:
            text = f.read()
            inp_stream = InputStream(text)
            lexer = MarkdownLexer(inp_stream)
            tokens = CommonTokenStream(lexer)
            parser = MarkdownParser(tokens)
            visitor = MarkdownAst(code_gen)
            visitor.visit(parser.program())
        return code_gen
