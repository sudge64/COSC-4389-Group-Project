"""
This program is for taking in a HTML file,
converting it to Markdown, and outputing the results
"""
import sys
import getopt
import re

def content(string, index, flag_end):
    """
    <content> ::= <element><content> | <element> | ∅
    """
    if re.match(r'^\s*$', string):
        print("Empty")
        return
    elif index == flag_end:
        index += 1
        markdown = element(string)
        content(string, index, flag_end)
        return markdown
    else:
        index += 1
        markdown = element(string)
        return markdown

def element(string):
    """
    <element> ::= <heading> | <paragraph> | <list>
    """
    if re.match(r".*<h[1-6][^>]*>.*<\/h[1-6]>", string):
        # This regex tests for HTML `header` tags
        return heading(string)
    elif re.match(r'.*<p[^>]*>.*<\/p>', string):
        # This regex tests for HTML `paragraph` tags
        return paragraph(string)
    elif re.match(r'.*<ul[^>]*>.*', string) or re.match(r'.*<ol[^>]*>.*', string):
        # This regex tests for HTML `li` tags
        return list_html(string)

def heading(string):
    """
    <heading> ::= "<h1>" <formattedText> "</h1>"
    | "<h2>" <formattedText> "</h2>"
    | "<h3>" <formattedText> "</h3>"
    | "<h4>" <formattedText> "</h4>"
    | "<h5>" <formattedText> "</h5>"
    | "<h6>" <formattedText> "</h6>"
    """
    clean_string = formatted_text(string)
    print(F"clean_string : {clean_string}")
    if re.match(r'.*<h1[^>]*>', string):
        # This regex tests for HTML `<h1>` tags
        clean_string = "# " + clean_string
        print(clean_string)
        return clean_string
    elif re.match(r'.*<h2[^>]*>', string):
        # This regex tests for HTML `<h2>` tags
        clean_string = "## " + clean_string
        print(clean_string)
        return clean_string
    elif re.match(r'.*<h3[^>]*>', string):
        # This regex tests for HTML `<h3>` tags
        clean_string = "### " + clean_string
        print(clean_string)
        return clean_string
    elif re.match(r'.*<h4[^>]*>', string):
        # This regex tests for HTML `<h4>` tags
        clean_string = "#### " + clean_string
        print(clean_string)
        return clean_string
    elif re.match(r'.*<h5[^>]*>', string):
        # This regex tests for HTML `<h5>` tags
        clean_string = "##### " + clean_string
        print(clean_string)
        return clean_string
    elif re.match(r'.*<h6[^>]*>', string):
        # This regex tests for HTML `<h6>` tags
        clean_string = "###### " + clean_string
        print(clean_string)
        return clean_string
    else:
        return

def paragraph(string):
    """
    <paragraph> ::= "<p>" <formattedText> "</p>"
    """
    clean_string = formatted_text(string)
    print(F"paragraph clean_string : {clean_string}")
    return clean_string

def list_html(string):
    """
    <list> ::= <unorderedList> | <orderedList>
    """
    if re.match(r'.*<ul[^>]*>.*', string):
        return list_unordered(string)
    elif re.match(r'.*<ol[^>]*>.*', string):
        return list_ordered(string)

def list_unordered(string):
    """
    <unorderedList> ::= "<ul>" (<listItem>)* "</ul>"
    """
    replace = "* "
    list_items = list_item(string, replace)
    for match in list_items:
        print(F"match : {match}")
    return ''.join([item + "\n" for item in list_items])


def list_ordered(string):
    """
    <orderedList> ::= "<ol>" (<listItem>)* "</ol>"
    """
    replace = "1. "
    list_items = list_item(string, replace)
    for i, match in enumerate(list_items, start=1):
        list_items[i-1] = f"\n{i}. {match[3:]}"
        # add the number and remove the opening <li> tag
        print(F"list_items : {list_items}")
    return ''.join([item + "\n" for item in list_items])

def list_item(string, replace):
    """
    <listItem> ::= "<li>" <formattedText> "</li>"
    """
    regex_list_item = re.compile(r'<li>(.*?)<\/li>')
    list_items = regex_list_item.findall(string)
    result_list_items = []
    for item in list_items:
        # This regex finds `<li>` tags
        clean_string = formatted_text(item)
        item_string = replace + clean_string
        result_list_items.append(item_string)
        print(F"item_string : {item_string}")
    return result_list_items

def formatted_text(string):
    """
    <formattedText> ::= <text> (<voidTag> | <containerTag>)*
    """
    void = r"<(?:area|base|br|col|embed|hr|img|input|keygen|link|meta|param|source|track|wbr)\s*/?>"
    if re.match(void, string):
        return void_tag(string)
    elif re.match(r"<(\w+)[^>]*>(.*?)<\/\1>", string):
        # This regex is to test if the opening and closing tags match
        return text(string)
    else:
        return container_tag(string)

def void_tag(string):
    """
    <voidTag> ::= "<area>" | "<base>" | "<br>"
    | "<col>" | "<embed>" | "<hr>"
    | "<img>" | "<input>"| "<keygen>"
    | "<link>" | "<meta>" | "<param>"
    | "<source>" | "<track>" | "<wbr>"
    """
    clean_string = clean_up(string)
    return clean_string

def container_tag(string):
    """
    <containerTag> ::= "<" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">" <formattedText>
    "</" ("code" | "b" | "strong" | "i" | "em" | "blockquote") ">"
    """
    while re.search(r'<(code|b|strong|i|em|blockquote)[^>]*>(.*?)<\/\1>', string):
        match = re.search(r'<(code|b|strong|i|em|blockquote)[^>]*>(.*?)<\/\1>', string)
        tag = match.group(1)
        holder = match.group(2)
        clean_holder = clean_up(holder)
        if tag == 'code':
            replacement = f"`{clean_holder}`"
        elif tag in ['b', 'strong']:
            replacement = f"**{clean_holder}**"
        elif tag in ['i', 'em']:
            replacement = f"*{clean_holder}*"
        elif tag == 'blockquote':
            replacement = f"\n> {clean_holder}\n"
        string = string[:match.start()] + replacement + string[match.end():]
    return clean_up(string)

def text(string):
    r"""
    <text> ::= [a-zA-Z0-9!@#$%^*()\-_=+`~,.\/?[\]{}\\|"\s]+
    """
    if re.match(r'^[A-Za-z0-9\s\,\.\?\`\~\!\@\#\$\%\^\&\*\(\)\-\_\=\+\|].*$', string):
        # This regex tests for upper- and lower-case letters, numbers, and special characters
        return clean_up(string)
    elif re.match(r'<!--.*?', string) or re.match(r'.*?-->', string):
        # This regex checks for HTML comments
        return None
    else:
        print("ERROR: String does not match text regex")
        return None

def clean_up(string):
    """
    Function to strip HTML tags and formatting whitespace from a string
    """
    no_whitespace = re.sub(r'^\s+', '', string)
    # This regex removes any whitespace characters from the beginning of a string
    no_opening_tags = re.sub(r'^<[^>]+>', '', no_whitespace)
    # This regex looks for any HTML opening tags
    no_closing_tags = re.sub(r'<\/[^>]+>$', '', no_opening_tags)
    # This regex looks for any HTML closing tags
    return no_closing_tags

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
        print(F"Line {i}: {current}", end="")
        if re.search('<body.*>', current):
            print("FOUND!")
            flag_start = i
        if re.search('</body.*>', current):
            print("FOUND!")
            flag_end = i
        i += 1
    print("\n")
    print(flag_start)
    print(flag_end)

    markdown_lines = []
    for index in range(flag_start+1,flag_end):
        print(F"Sending {list_of_lines[index]}")
        markdown_lines.append(content(list_of_lines[index], index, flag_end))

    markdown_lines = [x for x in markdown_lines if x is not None]
    print(F"markdown_lines : {markdown_lines}")
    return markdown_lines

def write(markdown_lines, file_output):
    """
    Function to read a file and write the contents to another file.
    """
    with open(file_output, 'w', encoding='UTF-8') as file_two:
        for line in markdown_lines:
            file_two.write(line)
        file_two.close()

def main(argv):
    """
    Main Function, handles reading arguments passed in from command line
    """
    input_file = ''
    output_file = ''
    opts, arg = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print('<filename>.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        else:
            print('Correct usage is: <filename>.py -i <inputfile> -o <outputfile>')
    print('Input file is', input_file)
    print('Output file is', output_file)
    write(open_file(input_file), output_file)

if __name__ == "__main__":
    main(sys.argv[1:])
