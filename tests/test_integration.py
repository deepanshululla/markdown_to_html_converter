import os

import pytest

from markdown_to_html_converter.semantics.markdown_converter import MarkdownToHtml


def populate_test_cases():
    test_files_root_dir = "./test_files"
    for root, dirnames, filenames in os.walk(test_files_root_dir):
        if root != test_files_root_dir:
            yield [os.path.join(root, "inp.md"), os.path.join(root, "out.html")]


@pytest.mark.parametrize("test_inp, exp_out_file",
                         populate_test_cases()
                         )
def test_overall_visitor(test_inp, exp_out_file):
    m = MarkdownToHtml(test_inp)
    codegen = m.parse()
    out_text = ""
    with open(exp_out_file) as f:
        out_text = f.read()

    exp_arr = out_text.strip('\n').strip('').split("\n")
    exp_arr = list(filter(lambda x: x != "", exp_arr))
    actual_arr = codegen.generate_code().strip('\n').split("\n")
    actual_arr = list(filter(lambda x: x != "", actual_arr))
    assert exp_arr == actual_arr
