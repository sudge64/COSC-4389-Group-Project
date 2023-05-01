"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os
import re

def contain(current):
    """
    <contain> ::= <cont><contain>
    """
    cont(current)
    contain(current)

def cont(current):
    """
    <cont> ::= <title> | <para> | <table> | <list> | ∅
    """
    if re.search('<h+[1-6].*>', current):
        print("FOUND! {current}", end="")
        title(current)
    elif re.search('<p.*>', current):
        para(current)
    elif re.search('<table.*>', current):
        table(current)
    elif re.search('<tr.*>', current):
        list_rule(current)
    else:
        print("Empty")

def title(current):
    """
    <title> ::= "<h1>" <formattedText> "</h1>" 
    | "<h2>" <formattedText> "</h2>" 
    | "<h3>" <formattedText> "</h3>" 
    | "<h4>" <formattedText> "</h4>" 
    | "<h5>" <formattedText> "</h5>" 
    | "<h6>" <formattedText> "</h6>"
    """
    if re.search('<h1.*>', current):
        print("Here's <h1.*>")
        formatted_text(current)
        if re.search('</h1.*>', current):
            print("Heading end", end="")

    if re.search('<h2.*>', current):
        print("Here's <h2.*>")
        formatted_text(current)
        if re.search('</h2.*>', current):
            print("Heading end", end="")

    if re.search('<h3.*>', current):
        print("Here's <h3.*>")
        formatted_text(current)
        if re.search('</h3.*>', current):
            print("Heading end", end="")

    if re.search('<h4.*>', current):
        print("Here's <h4.*>")
        formatted_text(current)
        if re.search('</4.*>', current):
            print("Heading end", end="")

    if re.search('<h5.*>', current):
        print("Here's <h5.*>")
        formatted_text(current)
        if re.search('</h5.*>', current):
            print("Heading end", end="")

    if re.search('<h6.*>', current):
        print("Here's <h6.*>")
        formatted_text(current)
        if re.search('</h6.*>', current):
            print("Heading end", end="")

def para(current):
    """
    <para> ::= "<p>"<text>"</p>" | "<p>"<formatted_text>"</p>"
    """
    if re.search('<p.*>', current):
        formatted_text(current)

def table(current):
    """
    <table> ::= "<table>"<table_row>"</table>"
    """
    if re.search('<table.*>', current):
        table_row(current)

def table_row(current):
    """
    <table_row> ::= "<tr>"<table_header>"</tr>" | "<tr>"<table_data>"</tr>"
    """
    if re.search('<tr.*>', current):
        table_header(current)

def table_header(current):
    """
    <table_header> ::= "<th>"<formatted_text>"</th>" | ∅
    """
    if re.search('<th.*>', current):
        formatted_text(current)
    else:
        print("Empty")

def table_data(current):
    """
    <table_data> ::= "<td>"<formatted_text>"</td>" | ∅
    """
    if re.search('<td.*>', current):
        formatted_text(current)
    else:
        print("Empty")

def list_rule(current):
    """
    (v2)<list> ::= <list_unordered> | <list_ordered>
    """
    if re.search('<ul.*>', current):
        list_unordered(current)
    if re.search('<ol.*>', current):
        list_ordered(current)

def list_unordered(current):
    """
    <list_unordered> ::= "<ul>"<list_item>"</ul>"
    """
    list_item(current)

def list_ordered(current):
    """
    <list_ordered> ::= "<ol>"<list_item>"</ol>"
    """
    list_item(current)

def list_item(current):
    """
    (v2)<list_item> ::= "<li>"<formatted_text>"</li>" | <list_item>"<li>"<formatted_text>"</li>"
    """
    if re.search('<li.*>', current):
        list_item(current)
        formatted_text(current)

def text(character):
    """
    <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m 
    | n | o | p | q | r | s | t | u | v | w | x | y | z 
    | A | B | C | D | E | F | G | H | I | J | K | L | M 
    | N | O | P | Q | R | S | T | U | V | W | X | Y | Z 
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
    | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + 
    | ` | ~ | , | . | / | ? [ | ] | { | } | \\ | "|"
    """
    pattern = re.compile(r'^[a-zA-Z0-9]+[^a-zA-Z0-9]$')
    if character in pattern:
        return True
    else:
        return False

def formatted_text(current):
    """
    <formatted_text> ::= <text><tag><formatted_text> | <text> | ∅
    """

    if text(current) and re.search('<.*>', current):
        tag(current)
        formatted_text(current)
    elif text(current):
        text(current)
    else:
        print("Empty")

def tag(current):
    """
    <tag> ::= <void_tag> | <container_tag>
    """

    if re.search('<.*>', current) and not re.search('</.*>', current):
        void_tag()
    else:
        container_tag(current)

def void_tag():
    """
    <void_tag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" 
    | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" 
    | "<param>" | "<source>" | "<track>" | "<wbr>"
    """
    void_tag_array = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>",
    "<img>", "<input>", "<keygen>", "<link>", "<meta>",
    "<param>", "<source>", "<track>", "<wbr>"]
    return void_tag_array

def container_tag(current):
    """
    (v2)<container_tag> ::= "<"<formatted_text_tag>">" <formatted_text> "</"\1">"
    """

    if re.search('<.*>', current) and not re.search('</.*>', current):
        formatted_text_tag()
        formatted_text(current)
        # closing tag

def formatted_text_tag():
    """
    # <formatted_text_tag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
    """
    tags = ["code", "b", "strong", "i", "em", "blockquote"]
    return tags

def open_file(file_input):
    """
    Function to open a file and save each line to a list
    """

    with open(file_input, 'r', encoding='UTF-8') as file_one:
        list_of_lines = file_one.readlines()
    file_one.close()

    # Need to only consider the HTML between <body> and </body>
    i = 0
    for current in list_of_lines:
        print("Line {i}: {current}", end="")
        # print(current, end=" ")

        if re.search('<body.*>', current):
            print("FOUND!")
            flag_start = i
            # contain(current)
        if re.search('</body.*>', current):
            print("FOUND!")
            flag_end = i
            # convert(file_input, file_output)
            # break
        i += 1
    print("\n")
    print(flag_start)
    print(flag_end)

    for index in range(flag_start,flag_end):
        contain(list_of_lines[index])

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
            if extension in output_file:
                with open('index.html', 'r', encoding='UTF-8') as index:
                    html = index.read()

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
    open_file(input_file)

def main(argv):
    """
    Main Function
    """
    read_command_line_args(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
