"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os
import re

# list_of_lines = []

# scanner
# def validate_lexemes():
#     global sentence
#     for lexeme in sentence:
#         if not valid_tag(lexeme):
#             return False
#     return True

def validate_tags(list_of_line):
    """
    Function to validate tags
    """
    # global line
    for tags in list_of_line:
        if not valid_tag(tags):
            return False
    return True

def valid_tag(tags):
    """
    Function to hold valid HTML tags.
    """
    return tags in ["h", "p", "table", "tr", "th", "td", "ul", "ol", "li"]

# def getNextLexeme():
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

def contain(list_of_line):
    """
    <contain> ::= <cont><contain>
    """

    cont(list_of_line)
    contain(list_of_line)

def cont(list_of_line):
    """
    <cont> ::= <title> | <para> | <table> | <list> | ∅
    """
    title(list_of_line)
    para(list_of_line)
    table(list_of_line)
    list_rule(list_of_line)

def title(list_of_line):
    """
    <title> ::= "<h"<title_number>">" <formatted_text> "</h"<title_number>">"
    """
    # global line
    if re.search('<h.*>', list_of_line):
        print("Here's <h.*>")
        title_number(list_of_line)
        formatted_text(list_of_line)
        if re.search('</h.*>', list_of_line):
            title_number(list_of_line)

def title_number(list_of_line):
    """
    <title_number> ::= 1 | 2 | 3 | 4 | 5 | 6
    """
    # global line
    if re.search('<h1.*>', list_of_line) or re.search('</h1.*>', list_of_line):
        return "1"
    if re.search('<h2.*>', list_of_line) or re.search('</h2.*>', list_of_line):
        return "2"
    if re.search('<h3.*>', list_of_line) or re.search('</h3.*>', list_of_line):
        return "3"
    if re.search('<h4.*>', list_of_line) or re.search('</h4.*>', list_of_line):
        return "4"
    if re.search('<h5.*>', list_of_line) or re.search('</h5.*>', list_of_line):
        return "5"
    if re.search('<h6.*>', list_of_line) or re.search('</h6.*>', list_of_line):
        return "6"

def para(list_of_line):
    """
    <para> ::= "<p>"<text>"</p>" | "<p>"<formatted_text>"</p>"
    """
    # global lexeme
    # global line
    if re.search('<p.*>', list_of_line):
        # valid_tag(list_of_line)
        valid_tag(list_of_line)
        formatted_text(list_of_line)

def table(list_of_line):
    """
    <table> ::= "<table>"<table_row>"</table>"
    """
    # global line
    if re.search('<table.*>', list_of_line):
        table_row(list_of_line)

def table_row(list_of_line):
    """
    <table_row> ::= "<tr>"<table_header>"</tr>" | "<tr>"<table_data>"</tr>"
    """
    # global line
    if re.search('<tr.*>', list_of_line):
        table_header(list_of_line)

def table_header(list_of_line):
    """
    <table_header> ::= "<th>"<formatted_text>"</th>" | ∅
    """
    # global line
    if re.search('<th.*>', list_of_line):
        formatted_text(list_of_line)

def table_data(list_of_line):
    """
    <table_data> ::= "<td>"<formatted_text>"</td>" | ∅
    """
    # global line
    if re.search('<td.*>', list_of_line):
        formatted_text(list_of_line)

def list_rule(list_of_line):
    """
    (v2)<list> ::= <list_unordered> | <list_ordered> // "This might work with (v2)<list_item> below."
    """
    # global line
    if re.search('<ul.*>', list_of_line):
        list_unordered(list_of_line)
    if re.search('<ol.*>', list_of_line):
        list_ordered(list_of_line)

def list_unordered(list_of_line):
    """
    <list_unordered> ::= "<ul>"<list_item>"</ul>" // "This needs to be recursive"
    """
    list_item(list_of_line)

def list_ordered(list_of_line):
    """
    <list_ordered> ::= "<ol>"<list_item>"</ol>" // "This needs to be recursive"
    """
    list_item(list_of_line)

def list_item(list_of_line):
    """
    (v2)<list_item> ::= "<li>"<formatted_text>"</li>" | <list_item>"<li>"<formatted_text>"</li>" // "This might work"
    """
    # global line
    if re.search('<li.*>', list_of_line):
        list_item(list_of_line)
        formatted_text(list_of_line)

# valid_tag()?
def text(character):
    """
    <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \\ | "|"
    """
    pattern = re.compile(r'^[a-zA-Z0-9]+[^a-zA-Z0-9]$')
    if character in pattern:
        return True
    else:
        return False
    # return character in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|", "", " "]

# TODO
def formatted_text(list_of_line):
    """
    <formatted_text> ::= <text><tag><formatted_text> | <text> | ∅
    """
    # global line
    if text(list_of_line):
        tag(list_of_line)
        formatted_text(list_of_line)

def tag(list_of_line):
    """
    <tag> ::= <void_tag> | <container_tag>
    """
    # global line
    if re.search('<.*>', list_of_line) and not re.search('</.*>', list_of_line):
        void_tag()
    else:
        container_tag(list_of_line)

def void_tag():
    """
    <void_tag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"
    """
    void_tag_array = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>", "<img>", "<input>", "<keygen>", "<link>", "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
    return void_tag_array

def container_tag(list_of_line):
    """
    (v2)<container_tag> ::= "<"<formatted_text_tag>">" <formatted_text> "</"\1">" // "Regex to force the same tag for opening and closing."
    """
    # global line
    if re.search('<.*>', list_of_line) and not re.search('</.*>', list_of_line):
    # if text(lexeme) == "<" and not text(lexeme) == "</":
        formatted_text_tag()
        formatted_text(list_of_line)
        # closing tag


def formatted_text_tag():
    """
    # <formatted_text_tag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
    """
    tags = ["code", "b", "strong", "i", "em", "blockquote"]
    return tags

def open_file(file_input, file_output):
    """
    Function to open a file and save each line to a list
    """
    # global line
    # global index

    # with open(file_input, 'r', encoding='UTF-8') as file_one:
    #     for index, line in enumerate(file_one):
    #         print("Line {}: {}".format(index, line.strip()))
    #         list_of_lines.append(line)
            # if re.search('<body.*>', line):
            #    print("FOUND!")
            #    contain()
    # file_one.close()

    with open(file_input, 'r', encoding='UTF-8') as file_one:
        list_of_lines = file_one.readlines()
    file_one.close()

    for iterator in list_of_lines:
        print(iterator)
        if re.search('<body.*>', iterator):
            print("FOUND!")
            contain(iterator)
        if re.search('</body.*>', iterator):
            print("FOUND!")
            convert(file_input, file_output)
            break

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
