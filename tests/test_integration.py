import os

import pytest

from markdown_to_html_converter.semantics.markdown_converter import MarkdownToHtml


def gen_tests():
    out_files = []
    test_files_root_dir = "./tests/test_files"
    inp_files = []
    for root, dirnames, filenames in os.walk(test_files_root_dir):
        if root != test_files_root_dir:
            inp_files.append(os.path.join(root, "inp.md"))
            out_files.append(os.path.join(root, "out.html"))
    return (inp_files, out_files)


inp_files, out_files = gen_tests()


@pytest.fixture(params=inp_files, scope="session")
def inp_file(request):
    return request.param


@pytest.fixture(params=out_files, scope="session")
def out_file(request):
    return request.param


@pytest.mark.parametrize("inp_file, out_file",
                         zip(*gen_tests()),
                         indirect=True
                         )
def test_overall_visitor(inp_file, out_file):
    m = MarkdownToHtml(inp_file)
    codegen = m.parse()
    out_text = ""
    with open(out_file) as f:
        out_text = f.read()

    # remove extraneous lines
    exp_arr = out_text.strip('\n').strip('').split("\n")
    exp_arr = list(filter(lambda x: x != "", exp_arr))
    actual_arr = codegen.generate_code().strip('\n').split("\n")
    actual_arr = list(filter(lambda x: x != "", actual_arr))
    # assert
    assert exp_arr == actual_arr
