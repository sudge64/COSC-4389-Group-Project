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
def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if not valid_tag(lexeme):
            return False
    return True

def valid_tag(lexeme):
    return lexeme in ["h", "p", "table", "tr", "th", "td", "ul", "ol", "li"]

def getNextLexeme():
    global lexeme
    global lexeme_index
    global sentence
    global num_lexemes
    global error

    lexeme_index = lexeme_index + 1
    if lexeme_index < num_lexemes:
        lexeme = sentence[lexeme_index]
    else:
        lexeme = " "

# Parser

def contain():
    """
    <contain> ::= <contain><cont>
    """
    contain()
    cont()

def cont():
    """
    <cont> ::= <title> | <para> | <table> | <list> | ∅
    """
    title()
    para()
    table()
    list_rule()

def title():
    """
    <title> ::= "<h"<title_number>">" <formatted_text> "</h"<title_number>">"
    """
    global lexeme
    global line
    if text(lexeme) == "<h":
        title_number()
        formatted_text()
        if text(lexeme) == "</h":
            title_number()

def title_number():
    """
    <title_number> ::= 1 | 2 | 3 | 4 | 5 | 6
    """
    heading_number = [1, 2, 3, 4, 5, 6]
    return heading_number

def para():
    """
    <para> ::= "<p>"<text>"</p>" | "<p>"<formatted_text>"</p>"
    """
    global lexeme
    global line
    if text(lexeme) == "<p>":
        valid_tag(lexeme)
        formatted_text()

def table():
    """
    <table> ::= "<table>"<table_row>"</table>"
    """
    global lexeme
    global line
    if text(lexeme) == "<table>":
        table_row()

def table_row():
    """
    <table_row> ::= "<tr>"<table_header>"</tr>" | "<tr>"<table_data>"</tr>"
    """
    global lexeme
    global line
    if text(lexeme) == "<tr>":
        table_header()

def table_header():
    """
    <table_header> ::= "<th>"<formatted_text>"</th>" | ∅
    """
    global lexeme
    global line
    if text(lexeme) == "<th>":
        formatted_text()

def table_data():
    """
    <table_data> ::= "<td>"<formatted_text>"</td>" | ∅
    """
    global lexeme
    global line
    if text(lexeme) == "<td>":
        formatted_text()

def list_rule():
    """
    (v2)<list> ::= <list_unordered> | <list_ordered> // "This might work with (v2)<list_item> below."
    """
    global lexeme
    global line
    if text(lexeme) == "<ul>":
        list_unordered()
    if text(lexeme) == "<ol>":
        list_ordered()

def list_unordered():
    """
    <list_unordered> ::= "<ul>"<list_item>"</ul>" // "This needs to be recursive"
    """
    list_item()

def list_ordered():
    """
    <list_ordered> ::= "<ol>"<list_item>"</ol>" // "This needs to be recursive"
    """
    list_item()

def list_item():
    """
    (v2)<list_item> ::= "<li>"<formatted_text>"</li>" | <list_item>"<li>"<formatted_text>"</li>" // "This might work"
    """
    global lexeme
    global line
    if text(lexeme) == "<li>":
        list_item()
        formatted_text()


# valid_tag()?
def text(lexeme):
    """
    <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \ | "|"
    """
    return lexeme in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|", "", " "]

def formatted_text():
    """
    <formatted_text> ::= <text><tag><formatted_text> | <text> | ∅
    """
    global lexeme
    global line
    if text(lexeme):
        tag()
        formatted_text()

def tag():
    """
    <tag> ::= <void_tag> | <container_tag>
    """
    global lexeme
    global line
    if text(lexeme) == "<" and not text(lexeme) == "</":
        void_tag()
    else:
        container_tag()

def void_tag():
    """
    <void_tag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"
    """
    void_tag_array = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>", "<img>", "<input>", "<keygen>", "<link>", "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
    return void_tag_array

def container_tag():
    # (v2)<container_tag> ::= "<"<formatted_text_tag>">" <formatted_text> "</"\1">" // "Regex to force the same tag for opening and closing."
    global lexeme
    global line
    if re.search('<.*>', line) and not re.search('</.*>', line):
    # if text(lexeme) == "<" and not text(lexeme) == "</":
        formatted_text_tag()
        formatted_text()
        # closing tag


def formatted_text_tag():
    # <formatted_text_tag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
    tags = ["code", "b", "strong", "i", "em", "blockquote"]
    return tags

def open_file(file_input, file_output):
    """
    Function to open a file
    """
    global line
    global index

    with open(file_input, 'r', encoding='UTF-8') as file_one:
        for index, line in enumerate(file_one):
            print("Line {}: {}".format(index, line.strip()))
            if re.search('<body.*>', line):
                print("FOUND!")

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
