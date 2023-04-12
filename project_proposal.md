# COSC: 4389 - Project Proposal

## Christian Wade

### Name of the project.

**Sledge** - The `Markdown` to `HTML` Converter.

### Members list.

Christian (C.J.) Wade

### General description.

Sledge is meant to be a `Markdown` to `HTML` converter equipped with the capability to convert `Markdown` files to `HTML` files and vice versa. It is intended to be a command line tool.

### Example of what is expected on using the system, if apply (inputs, output).

As Sledge is intended to be a CLI tool, it will be invoked as such. It will be given an input file and a file to output. It will not matter if the input file is a `Markdown` file or `HTML` file. It should return an error if the input and output file types match.

An example input:

`<file_name>.py -i <input_file_name>.extension -o <output_file_name>.extension`

### Limits (what the project is not expected to do).

Sledge is not intended to convert the idiosyncrasies of each language to the other, only the common, similar syntax.