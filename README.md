# Implemention of a Markdown => HTML converter

Markdown is a simple syntax used to generate formatted text. It’s used in lots
of places, but the one most developers have probably encountered is README
files in github.

For this exercise, I wrote a program which converts a small
subset of markdown to HTML. The final result is a cli which we can use.
This project is an attempt to create a translation engine
that uses Antlr to create grammar as well as the abstact syntax tree for our work.

## What we currently support/ Formatting Specifics

Markdown is a fairly rich specification; for this assignment, we’re only
looking for a small subset. This is the formatting we’d like you to implement:

| Markdown                               | HTML                                              |
| -------------------------------------- | ------------------------------------------------- |
| `# Heading 1`                          | `<h1>Heading 1</h1>`                              |
| `## Heading 2`                         | `<h2>Heading 2</h2>`                              |
| `...`                                  | `...`                                             |
| `###### Heading 6`                     | `<h6>Heading 6</h6>`                              |
| `Unformatted text`                     | `<p>Unformatted text</p>`                         |
| `[Link text](https://www.example.com)` | `<a href="https://www.example.com">Link text</a>` |
| `Blank line`                           | `Ignored`                                         |

### Demo

There are 2 ways to run everything
1) Using your own machine
The project requires setting up [antlr](https://www.antlr.org/) first.

then After cloning the repo, use
```bash
make run
```
This uses a default file.

However we can specify our own file

```bash
PYTHONPATH=.. python lang_bin.py --file="./tests/test_files/test1/inp.md"
```

Run integration tests
```bash
make tests
```

2) The second way is to use docker.

```bash
make docker_run
```
This uses a default file.

Run integration tests
```bash
make docker_run_tests
```

## Test Coverage

I created a small test framework to automatically do the integration testing. The only thing we need to do add more tests is to create a directory [here](./tests/test_files).
Then create 2 files which is our input and name in `inp.md` and the expected out file which will be named as `out.html`.
That's pretty much it to add new test cases.


```bash

(venv) ➜  markdown_to_html_converter git:(master) ✗ make test
PYTHONPATH=.. python -m pytest --cov=./semantics
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.9.7, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/deepanshululla/mycode/PycharmProjects/markdown_to_html_converter/markdown_to_html_converter
plugins: ordering-0.6, cov-3.0.0
collected 2 items

tests/test_integration.py ..                                                                                                                                         [100%]

---------- coverage: platform darwin, python 3.9.7-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
semantics/__init__.py                 0      0   100%
semantics/code_generator.py          12      2    83%
semantics/markdown_converter.py      19      0   100%
semantics/markdown_visitor.py        64      9    86%
-----------------------------------------------------
TOTAL                                95     11    88%


============================================================================ 2 passed in 0.33s =============================================================================
(
```


Here is an example template syntax [input file](./tests/test_files/test1/inp.md)
and the [generated output file](./out.html).
