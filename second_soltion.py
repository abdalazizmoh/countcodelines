#!/bin/python
import sys
import re
from os import path

def read_file_path():
    try:
        path = sys.argv[1]
    except IndexError as e:
        path = input('Please, Enter the file path: ')
    return path

# retrive the date from the file provide
def retrive_data_from_file(path):
    try:
        with open(path, 'r') as f:
            lines = f.read()
        return lines
    except IOError:
        print('Not valid input')
        sys.exit()


def count_code_line(lines):
    code_only_lines = ""
    character_count = 0
    total_line_count = 0
    code_length = len(lines)

    lines_zeros = [0]*len(lines)
    comments_match = re.compile(r'\/\*(\*(?!\/)|[^*])*\*\/')

    for comment_match in comments_match.finditer(lines):
        for index in range(comment_match.start(), comment_match.end()):
            if lines[index] != '\n':
                lines_zeros[index] = 1

    for charcter_index in range(len(lines)):
        if lines_zeros[charcter_index] == 1:            
            continue        
        code_only_lines = code_only_lines + lines[charcter_index]
    
    strings_multiline_match = re.compile(r'@\".*\"',re.DOTALL)

    for string_multiline_match in strings_multiline_match.finditer(code_only_lines):
        pointer = 0
        for index in range(string_multiline_match.start(),string_multiline_match.end()):
            new_postion = pointer + index
            if code_only_lines[new_postion] == '\n':
               code_only_lines = code_only_lines[:new_postion] + 'temp\n' + code_only_lines[new_postion:]
               pointer += 5

    linesWithoutSpace=code_only_lines.replace(' ','')

    code_only_inline = linesWithoutSpace.splitlines()
    for line in code_only_inline:
        if line.startswith('//'):
            continue
        if len(line) > 0:
            print(line)
            total_line_count = total_line_count + 1

    return total_line_count

# Call the functions in main  
if __name__ == "__main__":
    path = read_file_path()
    lines = retrive_data_from_file(path)
    count_code_line = count_code_line(lines)
    print("numner of code line", count_code_line)