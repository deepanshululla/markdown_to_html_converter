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
| **...**  (bold)                        |  <strong> ... </strong>                             |
| *...*     (italic)                     |  <i>  ...  </i>                                       |
| ***...**     (bolditalic)              |  <strong><i>  ...  </i></strong>                      |

### Demo

After cloning the repo, use
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

Here is an example template syntax [input file](./tests/test_files/test1/inp.md)
and the [generated output file](./out.html).
