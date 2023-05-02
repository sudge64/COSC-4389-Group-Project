"""
This program is for taking in a HTML file,
converting it to Markdown, and outputing the results
"""
import sys
import getopt
import webbrowser
import os
import re

def content(string):
    """
    <content> ::= <element><content> | <element> | ∅
    """
    if re.match('^*', string):
        print("Empty")
        return
    elif re.match('pattern', string):
        element()
    else:
        element()
        content()

def element():
    """
    <element> ::= <title> | <paragraph> | <table> | <list>
    """
    title()
    paragraph()
    table()
    list_html()

def title():
    """
    <title> ::= "<h1>" <formattedText> "</h1>" | "<h2>" <formattedText> "</h2>" | "<h3>" <formattedText> "</h3>" | "<h4>" <formattedText> "</h4>" | "<h5>" <formattedText> "</h5>" | "<h6>" <formattedText> "</h6>"
    """

def paragraph():
    """
    <paragraph> ::= "<p>" <formattedText> "</p>"
    """

def table():
    """
    <table> ::= "<table>" <tableRow> "</table>"
    """

def table_row():
    """
    <tableRow> ::= "<tr>" (<tableHeader> | <tableData>)* "</tr>"
    """

def table_header():
    """
    <tableHeader> ::= "<th>" <formattedText> "</th>"
    """

def table_data():
    """
    <tableData> ::= "<td>" <formattedText> "</td>"
    """

def list_html():
    """
    <list> ::= <unorderedList> | <orderedList>
    """

def list_unordered():
    """
    <unorderedList> ::= "<ul>" (<listItem>)* "</ul>"
    """

def list_ordered():
    """
    <orderedList> ::= "<ol>" (<listItem>)* "</ol>"
    """

def list_item():
    """
    <listItem> ::= "<li>" <formattedText> "</li>"
    """

def formatted_text():
    """
    <formattedText> ::= <text> (<voidTag> | <containerTag>)*
    """

def container_tag():
    """
    <containerTag> ::= "<" <formattedTextTag> ">" <formattedText> "</" \1 ">"
    """

def formatted_text_tag():
    """
    <formattedTextTag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"
    """

def void_tag():
    """
    <voidTag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"
    """

def text():
    """
    <text> ::= [a-zA-Z0-9!@#$%^*()\-_=+`~,.\/?[\]{}\\|"\s]+
    """

def open_file(file_input, file_output):
    """
    Function to open a file and save each line to a list
    """

    with open(file_input, 'r', encoding='UTF-8') as file_one:
        list_of_lines = file_one.readlines()
    file_one.close()

    # Need to only consider the HTML between <body> and </body>
    i = 0
    for current in list_of_lines:
        print(F"Line {i}: {current}", end="")
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

    for index in range(flag_start+1,flag_end):
        print(F"Sending {list_of_lines[index]}")
        convert(list_of_lines[index], file_output)

def convert(list_of_lines, file_output):
    """
    Function to read a file and write the contents to another file.
    """
    with open(file_output, 'w', encoding='UTF-8') as file_two:
        for line in list_of_lines:
            file_two.write(line)
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
    open_file(input_file, output_file)

def main(argv):
    """
    Main Function
    """
    read_command_line_args(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
