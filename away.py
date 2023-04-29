"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os

# Arrays to hold HTML tags.

# html_tags_heading_opening = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>"]
# html_tags_closing_closing = ["</h1>", "</h2>", "</h3>", "</h4>", "</h5>", "</h6>"]
# html_tags_list_opening = ["<ul>", "<ol>", "<li>"]
# html_tags_list_closing = ["</ul>", "</ol>", "</li>"]
# html_tags_table_opening = ["<table>", "<tr>", "<th>", "<td>"]
# html_tags_table_closing = ["</table>", "</tr>", "</th>", "</td>"]
# html_tags_text_opening = ["<p>", "<q>", "<body>", "<a>", "<code>", "<br>", "<img>", "<b>", "<strong>", "<i>", "<em>", "<blockquote>"]
# html_tags_text_closing = ["</p>", "</q>", "</body>", "</a>", "</code>", "</b>", "</strong>", "</i>", "</em>", "</blockquote>"]


# scanner
def validate_lexemes():
    global sentence
    for lexeme in sentence:
        if not valid_lexeme(lexeme):
            return False
    return True


def valid_lexeme(lexeme):
    return lexeme in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|"]
# Add empty as valid lexeme

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

# <contain> ::= <contain><cont>
def contain():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    contain()
    cont()

# <cont> ::= <title> | <para> | <table> | <list> | ∅
def cont():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    title()
    para()
    table()
    list_rule()

# <title> ::= "<h"<title_number>">" <formatted_text> "</h"<title_number>">"
def title():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<h":
        title_number()
        formatted_text()
        if text(lexeme) == "</h":
            title_number()

# <title_number> ::= 1 | 2 | 3 | 4 | 5 | 6
def title_number():
    heading_number = [1, 2, 3, 4, 5, 6]
    return heading_number

# <para> ::= "<p>"<text>"</p>" | "<p>"<formatted_text>"</p>"
def para():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<p>":
        valid_lexeme(lexeme)
        formatted_text()

# <table> ::= "<table>"<table_row>"</table>"
def table():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<table>":
        table_row()

# <table_row> ::= "<tr>"<table_header>"</tr>" | "<tr>"<table_data>"</tr>"
def table_row():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<tr>":
        table_header()

# <table_header> ::= "<th>"<formatted_text>"</th>" | ∅
def table_header():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<th>":
        formatted_text()

# <table_data> ::= "<td>"<formatted_text>"</td>" | ∅
def table_data():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<td>":
        formatted_text()

# (v2)<list> ::= <list_unordered> | <list_ordered> // "This might work with (v2)<list_item> below."
def list_rule():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<ul>":
        list_unordered()
    if text(lexeme) == "<ol>":
        list_ordered()

# <list_unordered> ::= "<ul>"<list_item>"</ul>" // "This needs to be recursive"
def list_unordered():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter
    
    list_item()

# <list_ordered> ::= "<ol>"<list_item>"</ol>" // "This needs to be recursive"
def list_ordered():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    list_item()

# (v2)<list_item> ::= "<li>"<formatted_text>"</li>" | <list_item>"<li>"<formatted_text>"</li>" // "This might work"
def list_item():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<li>":
        list_item()
        formatted_text()

# <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \ | "|"
# valid_lexeme()
def text(lexeme):
    return lexeme in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|"]

# <formatted_text> ::= <text><tag><formatted_text> | <text> | ∅
def formatted_text():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme):
        tag()
        formatted_text()

# <tag> ::= <void_tag> | <container_tag>
def tag():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<" and not text(lexeme) == "</":
        void_tag()
    else:
        container_tag()

# <void_tag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"
def void_tag():
    void_tag_array = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>", "<img>", "<input>", "<keygen>", "<link>", "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
    return void_tag_array

# (v2)<container_tag> ::= "<"<formatted_text_tag>">" <formatted_text> "</"\1">" // "Regex to force the same tag for opening and closing."
def container_tag():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if text(lexeme) == "<" and not text(lexeme) == "</":
        formatted_text_tag()
        formatted_text()
        # closing tag

# <formatted_text_tag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
def formatted_text_tag():
    tags = ["code", "b", "strong", "i", "em", "blockquote"]
    return tags

def open_file(file_input, file_output):
    """
    Function to open a file
    """
    with open(file_input, 'r', encoding='UTF-8') as file_one:
        for index, line in enumerate(file_one):
            print("Line {}: {}".format(index, line.strip()))

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
