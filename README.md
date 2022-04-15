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
```bash

docker run deepanshululla/jinja_clone

```

To use this in your custom project, you need to have exactly
one json(namespace params) and template file.

```bash
echo MY_DIR_LOCATION="my location for files"

docker run  -v $MY_DIR_LOCATION:/data deepanshululla/jinja_clone --directory=/data

```
Alternative you can clone the repo and do
```bash
make run
```

Run integration tests
```bash
make tests
```

Here is an example template syntax [template_file](./test_files/test1/inp.md)
and the [generated output file](./out.html).
