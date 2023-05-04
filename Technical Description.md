# COSC: 4389 - Project

# Technical Description - `away.py`

## Author: Christian Wade

### Grammar

```EBNF
<content> ::= <element><content> | <element> | ∅

<element> ::= <heading> | <paragraph> | <list>

<heading> ::= "<h1>" <formattedText> "</h1>" | "<h2>" <formattedText> "</h2>" | "<h3>" <formattedText> "</h3>" | "<h4>" <formattedText> "</h4>" | "<h5>" <formattedText> "</h5>" | "<h6>" <formattedText> "</h6>"

<paragraph> ::= "<p>" <formattedText> "</p>"

<list> ::= <unorderedList> | <orderedList>
<unorderedList> ::= "<ul>" (<listItem>)* "</ul>"
<orderedList> ::= "<ol>" (<listItem>)* "</ol>"
<listItem> ::= "<li>" <formattedText> "</li>"

<formattedText> ::= <text> (<voidTag> | <containerTag>)*
<containerTag> ::= "<" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">"<formattedText> "</" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">"
<voidTag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"

<text> ::= [a-zA-Z0-9!@#$%^*()\-_=+`~,.\/?[\]{}\\|"\s]+
```

<div style="page-break-after: always;"></div>

### Modules

```Python
"""
This program is for taking in a HTML file,
converting it to Markdown, and outputing the results
"""
```
```Python
def content(string, index, flag_end):
	"""
	<content> ::= <element><content> | <element> | ∅
	"""
```
```Python
def element(string):
	"""
	<element> ::= <heading> | <paragraph> | <list>
	"""
```
```Python
def heading(string):
	"""
	<heading> ::= "<h1>" <formattedText> "</h1>"
	| "<h2>" <formattedText> "</h2>"
	| "<h3>" <formattedText> "</h3>"
	| "<h4>" <formattedText> "</h4>"
	| "<h5>" <formattedText> "</h5>"
	| "<h6>" <formattedText> "</h6>"
	"""
```
```Python
def paragraph(string):
	"""
	<paragraph> ::= "<p>" <formattedText> "</p>"
	"""
```
```Python
def list_html(string):
	"""
	<list> ::= <unorderedList> | <orderedList>
	"""
```
```Python
def list_unordered(string):
	"""
	<unorderedList> ::= "<ul>" (<listItem>)* "</ul>"
	"""
```

<div style="page-break-after: always;"></div>

```Python
def list_ordered(string):
	"""
	<orderedList> ::= "<ol>" (<listItem>)* "</ol>"
	"""
```
```Python
def list_item(string, replace):
	"""
	<listItem> ::= "<li>" <formattedText> "</li>"
	"""
```
```Python
def formatted_text(string):
	"""
	<formattedText> ::= <text> (<voidTag> | <containerTag>)*
	"""
```
```Python
def void_tag(string):
	"""
	<voidTag> ::= "<area>" | "<base>" | "<br>"
	| "<col>" | "<embed>" | "<hr>"
	| "<img>" | "<input>"| "<keygen>"
	| "<link>" | "<meta>" | "<param>"
	| "<source>" | "<track>" | "<wbr>"
	"""
```
```Python
def container_tag(string):
	"""
	<containerTag> ::= "<" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">" <formattedText>
	"</" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">"
	"""
```
```Python
def text(string):
	r"""
	<text> ::= [a-zA-Z0-9!@#$%^*()\-_=+`~,.\/?[\]{}\\|"\s]+
	"""
```
```Python
def clean_up(string):
	"""
	Function to strip HTML tags and formatting whitespace from a string
	"""
```

<div style="page-break-after: always;"></div>

```Python
def open_file(file_input):
	"""
	Function to open a file and save each line to a list
	"""
```
```Python
def write(markdown_lines, file_output):
	"""
	Function to read a file and write the contents to another file.
	"""
```
```Python
def main(argv):
	"""
	Main Function, handles reading arguments passed in from command line
	"""
```

<div style="page-break-after: always;"></div>