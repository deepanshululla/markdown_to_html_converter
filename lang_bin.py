from argparse import ArgumentParser

from markdown_to_html_converter.semantics.markdown_converter import MarkdownToHtml


def parse_args():
    parser = ArgumentParser(description='markdown to html DSL interpreter')
    parser.add_argument("-f", "--file", type=str, help="file to parse")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if not args.file:
        md_file = './tests/test_files/test2/inp.md'
    else:
        md_file = args.directory

    m = MarkdownToHtml(md_file)
    code_gen = m.parse()
    print(code_gen.generate_code())
    code_gen.write_to("out.html")
