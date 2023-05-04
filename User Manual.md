# COSC: 4389 - Project

# User Manual - `away.py`

## Author: Christian Wade

### How to use the system

As **Away** is intended to be a command line tool, it will be invoked as such. It will be given an input file and a file to write the output. The input file is expected to be a `HTML` file, the output file is expected to be a `Markdown` file.

An example input is as follows:

`python3 away.py -i <input_file_name>.html -o <output_file_name>.md`

If you run the program with the help option `python3 away.py -h`, this will be the output: `<filename>.py -i <inputfile> -o <outputfile>`

<div style="page-break-after: always;"></div>

### Examples of Input

It is important to note that `<ul>` and `<ol>` tags must be on the same line as their closing tags and all the `<li></li>` tags that they enclose.

#### `test.html`

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
<title>Index</title>
<meta charset="utf-8">
<link rel="stylesheet" href="styles.css">
</head>
<body class="body">
<h1 class="text">Heading 1</h1>
<h2 class="text">Heading 2</h2>
<h3 class="text">Heading 3</h3>
<h4 class="text">Heading 4</h4>
<h5 class="text">Heading 5</h5>
<h6 class="text">Heading 6</h6>
<p class="text"><b>This</b> is a <i>test</i> paragraph.<code>print("Hello World!")</code><blockquote class="text">With a blockquote</blockquote></p>
<ul class="text"><li>Item 1</li><li>Item 2</li></ul>
<ol class="text"><li>Item 1</li><li>Item 2</li></ol>
<!--table class="text">
</table-->
</body>
</html>
```

<div style="page-break-after: always;"></div>

### Examples of Output

#### `test.md`

```Markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
**This** is a *test* paragraph.`print("Hello World!")`
> With a blockquote
* Item 1
* Item 2

1. Item 1

2. Item 2
```

When converting from `HTML` to `Markdown`, everything before the first `<body>` tag is disregarded. If converting from `Markdown` to `HTML`, then everything before the first `<body>` tag would be added.

<div style="page-break-after: always;"></div>