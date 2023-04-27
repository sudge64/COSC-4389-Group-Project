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
      if (not valid_lexeme(lexeme)):
         return False
   return True


def valid_lexeme(lexeme):
    return lexeme in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",  "p",  "q",  "r",  "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "!" , "@" , "#" , "$" , "%" , "^" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "`" , "~" , "," , "." , "/" , "?", "[" , "]" , "{" , "}" , "\"", "|"]


def getNextLexeme():
   global lexeme
   global lexeme_index
   global sentence
   global num_lexemes
   global error

   lexeme_index = lexeme_index + 1
   if (lexeme_index < num_lexemes):
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
    list()

# <title> ::= "<h"<titleNumber>">" <formattedText> "</h"<titleNumber>">"

def title():
    global lexeme
    global lexeme_index
    global num_lexemes
    global lexeme_counter

    if lexeme == "<h":
        titleNumber()

# <titleNumber> ::= 1 | 2 | 3 | 4 | 5 | 6

def titleNumber():
    heading_number = [1, 2, 3, 4, 5, 6]
    return heading_number

# <para> ::= "<p>"<text>"</p>" | "<p>"<formattedText>"</p>"

# <table> ::= "<table>"<tableRow>"</table>"
# <tableRow> ::= "<tr>"<tableHeader>"</tr>" | "<tr>"<tableData>"</tr>"
# <tableHeader> ::= "<th>"<formattedText>"</th>" | ∅
# <tableData> ::= "<td>"<formattedText>"</td>" | ∅


# (v2)<list> ::= <listUnordered> | <listOrdered> // "This might work with (v2)<listItem> below."
# <listUnordered> ::= "<ul>"<listItem>"</ul>" // "This needs to be recursive"
# <listOrdered> ::= "<ol>"<listItem>"</ol>" // "This needs to be recursive"
# (v2)<listItem> ::= "<li>"<formattedText>"</li>" | <listItem>"<li>"<formattedText>"</li>" // "This might work"

# <text> ::=  a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ! | @ | # | $ | % | ^ | * | ( | ) | - | _ | = | + | ` | ~ | , | . | / | ? [ | ] | { | } | \ | "|"
# <formattedText> ::= <text><tag><formattedText> | <text> | ∅
# <tag> ::= <voidTag> | <containerTag>
# <voidTag> ::= "<area>" | "<base>" | "<br>" | "<col>" | "<embed>" | "<hr>" | "<img>" | "<input>" | "<keygen>" | "<link>" | "<meta>" | "<param>" | "<source>" | "<track>" | "<wbr>"


# (v2)<containerTag> ::= "<"<formattedTextTag>">" <formattedText> "</"\1">" // "Regex to force the same tag for opening and closing."
# <formattedTextTag> ::= "code" | "b" | "strong" | "i" | "em" | "blockquote"


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


def main(argv):
    """
    Main Function
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
    convert(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
    while 1:
        line = input('Enter expression: ')
        #  line = line[:-1]   # remove trailing newline
        sentence = line.split()

        num_lexemes = len(sentence)

        lexeme_index = -1
        error = False

        if validate_lexemes():
            getNextLexeme()
            # symbol_expr()

            # Either an error occurred or
            # the input sentence is not entirely parsed.
            if (error or lexeme_index < num_lexemes):
                print('"{}" is not a sentence.'.format(line))
            else:
                print('"{}" is a sentence.'.format(line))
        else:
            print('"{}" contains invalid lexemes and, thus, '
                    'is not a sentence.'.format(line))
