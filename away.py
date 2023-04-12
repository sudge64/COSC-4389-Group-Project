"""
This program is for taking in a Markdown or HTML file,
translating between the two, and outputing the results
"""
import sys
import getopt
import webbrowser
import os

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
    opts, arg = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print('<filename>.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt == "-b":
            # This causes a program crash. Something about the `-b` is not recognized.
            extension = ".html"
            if extension in input_file or extension in output_file:
                with open('index.html', 'r',encoding='UTF-8') as index:
                    html = index.read()

                path = os.path.abspath(output_file+'.html')
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
