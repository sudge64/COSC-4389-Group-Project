# COSC: 4389 - Project Proposal

## Christian Wade

### Name of the project

**Away** - The `Markdown` to `HTML` Converter.

### Members list

Christian (C.J.) Wade

### General description

**Away** is meant to be a `Markdown` to `HTML` converter equipped with the capability to convert `Markdown` files to `HTML` files and vice versa. It is intended to be a command line tool.

It is named **Away** because `Markdown` and `HTML` are both mark_up_ languages and this tool is meant to be useful and enable its users to reach new _heights_ of convenience. Thus, the phrase, "Up, Up, and **Away**."

### Example of what is expected on using the system, if apply (inputs, output)

As **Away** is intended to be a CLI tool, it will be invoked as such. It will be given an input file and a file to output. It will not matter if the input file is a `Markdown` file or `HTML` file. It should return an error if the input and output file types match.

#### An example command line input:

`<file_name>.py -i <input_file_name>.extension -o <output_file_name>.extension`

<div style="page-break-after: always;"></div>

#### An example `HTML` input file:

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
<title>Index</title>
<meta charset="utf-8">
<link rel="stylesheet" href="styles.css">
</head>
<body>
	<h1>Heading 1</h1>
	<p>This is a test <br>paragraph.</p>
	<ul><li>Item 1</li><li>Item 2</li></ul>
</body>
</html>
```

#### An example `Markdown` output file:

```Markdown
# Heading 1

This is a test  
paragraph.

* Item 1

* Item 2
```

When converting from `HTML` to `Markdown`, everything before the first `<body>` tag is disregarded. If converting from `Markdown` to `HTML`, then everything before the first `<body>` tag would be added.

### Limits (what the project is not expected to do)

**Away** is not intended to convert the idiosyncrasies of each language to the other, only the common, similar syntax.
