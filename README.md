# COSC-4389-Group-Project

This repository is for the Group Project for COSC 4389. It is a `HTML` to `Markdown` converter written in `Python`. It is meant to take in either a `HTML` or `Markdown` file and output one or the other.

It's command line syntax is `python3 <filename>.py -i <inputfile> -o <outputfile>`.

## Proposal

### Name of the project

**Away** - The `Markdown` to `HTML` Converter.

### General description

**Away** is meant to be a `Markdown` to `HTML` converter equipped with the capability to convert `Markdown` files to `HTML` files and vice versa. It is intended to be a command line tool.

It is named **Away** because `Markdown` and `HTML` are both mark_up_ languages and this tool is meant to be useful and enable its users to reach new _heights_ of convenience. Thus, the phrase, "Up, Up, and **Away**."

### Example of what is expected on using the system, if apply (inputs, output)

As **Away** is intended to be a CLI tool, it will be invoked as such. It will be given an input file and a file to output. It will not matter if the input file is a `Markdown` file or `HTML` file. It should return an error if the input and output file types match.

An example input:

`<file_name>.py -i <input_file_name>.extension -o <output_file_name>.extension`

### Limits (what the project is not expected to do)

**Away** is not intended to convert the idiosyncrasies of each language to the other, only the common, similar syntax.

## Grammar

Here is the grammar that **Away** uses for `HTML` to `Markdown` conversion:

```EBNF
<contain> ::= <cont><contain>
<cont> ::= <title> | <para> | <table> | <list> | ∅

<title> ::= "<h"<titleNumber>">" <formattedText> "</h"<titleNumber>">"
<titleNumber> ::= 1 | 2 | 3 | 4 | 5 | 6

<para> ::= "<p>"<text>"</p>" | "<p>"<formattedText>"</p>"

<table> ::= "<table>"<tableRow>"</table>"
<tableRow> ::= "<tr>"<tableHeader>"</tr>" | "<tr>"<tableData>"</tr>"
<tableHeader> ::= "<th>"<formattedText>"</th>" | ∅
<tableData> ::= "<td>"<formattedText>"</td>" | ∅

(v2)<list> ::= <listUnordered> | <listOrdered> // "This might work with (v2)<listItem> below."
<listUnordered> ::= "<ul>"<listItem>"</ul>" // "This needs to be recursive"
<listOrdered> ::= "<ol>"<listItem>"</ol>" // "This needs to be recursive"
(v2)<listItem> ::= "<li>"<formattedText>"</li>" | <listItem>"<li>"<formattedText>"</li>" // "This might work"

<text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \ | "|"
<formattedText> ::= <text><tag><formattedText> | <text> | ∅
<tag> ::= <voidTag> | <containerTag>
<voidTag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"

(v2)<containerTag> ::= "<"<formattedTextTag>">" <formattedText> "</"\1">" // "Regex to force the same tag for opening and closing."
<formattedTextTag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
```
