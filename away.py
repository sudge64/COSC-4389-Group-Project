"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os
import re

# scanner
# def validate_lexemes():
#     global sentence
#     for lexeme in sentence:
#         if not valid_tag(lexeme):
#             return False
#     return True

def validate_tags(line):
    # global line
    for tags in line:
        if not valid_tag(tags):
            return False
    return True

def valid_tag(tags):
    return tags in ["h", "p", "table", "tr", "th", "td", "ul", "ol", "li"]

# def getNextLexeme(line):
#     global lexeme
#     global lexeme_index
#     global sentence
#     global num_lexemes
#     global error
#
#     lexeme_index = lexeme_index + 1
#     if lexeme_index < num_lexemes:
#         lexeme = line[lexeme_index]
#     else:
#         lexeme = " "

# Parser

def contain(line):
    """
    <contain> ::= <cont><contain>
    """

    cont(line)
    contain(line)

def cont(line):
    """
    <cont> ::= <title> | <para> | <table> | <list> | ∅
    """
    title(line)
    para(line)
    table(line)
    list_rule(line)

def title(line):
    """
    <title> ::= "<h"<title_number>">" <formatted_text> "</h"<title_number>">"
    """
    # global line
    if re.search(r'<h.*>', line):
        print("Here's <h.*>")
        title_number(line)
        formatted_text(line)
        if re.search(r'</h.*>', line):
            title_number(line)

def title_number(line):
    """
    <title_number> ::= 1 | 2 | 3 | 4 | 5 | 6
    """
    # global line
    if re.search('<h1.*>', line) or re.search('</h1.*>', line):
        return "1"
    if re.search('<h2.*>', line) or re.search('</h2.*>', line):
        return "2"
    if re.search('<h3.*>', line) or re.search('</h3.*>', line):
        return "3"
    if re.search('<h4.*>', line) or re.search('</h4.*>', line):
        return "4"
    if re.search('<h5.*>', line) or re.search('</h5.*>', line):
        return "5"
    if re.search('<h6.*>', line) or re.search('</h6.*>', line):
        return "6"

def para(line):
    """
    <para> ::= "<p>"<text>"</p>" | "<p>"<formatted_text>"</p>"
    """
    global lexeme
    # global line
    if re.search('<p.*>', line):
        valid_tag(lexeme)
        formatted_text(line)

def table(line):
    """
    <table> ::= "<table>"<table_row>"</table>"
    """
    # global line
    if re.search('<table.*>', line):
        table_row(line)

def table_row(line):
    """
    <table_row> ::= "<tr>"<table_header>"</tr>" | "<tr>"<table_data>"</tr>"
    """
    # global line
    if re.search('<tr.*>', line):
        table_header(line)

def table_header(line):
    """
    <table_header> ::= "<th>"<formatted_text>"</th>" | ∅
    """
    # global line
    if re.search('<th.*>', line):
        formatted_text(line)

def table_data(line):
    """
    <table_data> ::= "<td>"<formatted_text>"</td>" | ∅
    """
    # global line
    if re.search('<td.*>', line):
        formatted_text(line)

def list_rule(line):
    """
    (v2)<list> ::= <list_unordered> | <list_ordered> // "This might work with (v2)<list_item> below."
    """
    # global line
    if re.search('<ul.*>', line):
        list_unordered(line)
    if re.search('<ol.*>', line):
        list_ordered(line)

def list_unordered(line):
    """
    <list_unordered> ::= "<ul>"<list_item>"</ul>" // "This needs to be recursive"
    """
    list_item(line)

def list_ordered(line):
    """
    <list_ordered> ::= "<ol>"<list_item>"</ol>" // "This needs to be recursive"
    """
    list_item(line)

def list_item(line):
    """
    (v2)<list_item> ::= "<li>"<formatted_text>"</li>" | <list_item>"<li>"<formatted_text>"</li>" // "This might work"
    """
    # global line
    if re.search('<li.*>', line):
        list_item(line)
        formatted_text(line)


# valid_tag()?
def text(character):
    """
    <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \ | "|"
    """
    return character in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|", "", " "]

# TODO
def formatted_text(line):
    """
    <formatted_text> ::= <text><tag><formatted_text> | <text> | ∅
    """
    # global line
    if text(line):
        tag(line)
        formatted_text(line)

def tag(line):
    """
    <tag> ::= <void_tag> | <container_tag>
    """
    # global line
    if re.search('<.*>', line) and not re.search('</.*>', line):
        void_tag()
    else:
        container_tag(line)

def void_tag():
    """
    <void_tag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"
    """
    void_tag_array = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>", "<img>", "<input>", "<keygen>", "<link>", "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
    return void_tag_array

def container_tag(line):
    # (v2)<container_tag> ::= "<"<formatted_text_tag>">" <formatted_text> "</"\1">" // "Regex to force the same tag for opening and closing."
    # global line
    if re.search('<.*>', line) and not re.search('</.*>', line):
    # if text(lexeme) == "<" and not text(lexeme) == "</":
        formatted_text_tag()
        formatted_text(line)
        # closing tag


def formatted_text_tag():
    # <formatted_text_tag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
    tags = ["code", "b", "strong", "i", "em", "blockquote"]
    return tags

def open_file(file_input, file_output):
    """
    Function to open a file
    """
    # global line
    global index

    with open(file_input, 'r', encoding='UTF-8') as file_one:
        for index, line in enumerate(file_one):
            print("Line {}: {}".format(index, line.strip()))
            if re.search('<body.*>', line):
                print("FOUND!")
                contain(line)
    file_one.close()

def convert(file_input, file_output):
    """
    Function to read a file and write the contents to another file.
    """
    with open(file_input, 'r', encoding='UTF-8') as file_one:
        with open(file_output, 'w', encoding='UTF-8') as file_two:
            for line in file_one:
                file_two.write(line)
        file_one.close()
        file_two.close()


def read_command_line_args(argv):
    """
    Function to read arguments passed in from command line
    """
    input_file = ''
    output_file = ''
    opts, arg = getopt.getopt(argv, "hi:o:b", ["ifile=", "ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print('<filename>.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in "-b":
            extension = ".html"
            # if extension in input_file or extension in output_file:
            if extension in output_file:
                with open('index.html', 'r', encoding='UTF-8') as index:
                    html = index.read()

                # path = os.path.abspath(output_file+'.html')
                path = os.path.abspath(output_file)
                url = 'file://' + path

                with open(path, 'w', encoding='UTF-8') as opened_file:
                    opened_file.write(html)
                    webbrowser.open(url)
            else:
                print("No html file found.")
        else:
            print('Correct usage is: <filename>.py -i <inputfile> -o <outputfile>')
    print('Input file is', input_file)
    print('Output file is', output_file)
    # convert(input_file, output_file)
    open_file(input_file, output_file)

def main(argv):
    """
    Main Function
    """
    read_command_line_args(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
