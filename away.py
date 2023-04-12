"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os

# Arrays to hold HTML tags.

html_tags_heading_opening = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>"]
html_tags_closing_closing = ["</h1>", "</h2>", "</h3>", "</h4>", "</h5>", "</h6>"]
html_tags_list_opening = ["<ul>", "<ol>", "<li>"]
html_tags_list_closing = ["</ul>", "</ol>", "</li>"]
html_tags_table_opening = ["<table>", "<tr>", "<th>", "<td>"]
html_tags_table_closing = ["</table>", "</tr>", "</th>", "</td>"]
html_tags_text_opening = ["<p>", "<q>", "<body>", "<a>", "<code>", "<br>"]
html_tags_text_closing = ["</p>", "</q>", "</body>", "</a>", "</code>"]

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
    opts, arg = getopt.getopt(argv,"hi:o:b",["ifile=","ofile="])
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
                with open('index.html', 'r',encoding='UTF-8') as index:
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
