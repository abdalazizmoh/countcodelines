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

'''def count_space_line(lines):
    count_empty_line = 0
    code_only_inline = lines.splitlines()
    for line in code_only_inline:
        lineWithoutSpace = line.strip()
        if not lineWithoutSpace:
            count_empty_line = count_empty_line +1
    return count_empty_line
'''

def count_code_line(lines):
    code_only_lines = ""
    character_count = 0
    total_line_count = 0
    linesWithoutSpace=lines.replace(' ','')
    code_length = len(linesWithoutSpace)

    while character_count < code_length:
        if character_count + 1 < code_length and linesWithoutSpace[character_count] == '/' and linesWithoutSpace[character_count + 1] == '*':
            character_count = character_count + 2
            while character_count < code_length:
                if character_count + 1 < code_length and linesWithoutSpace[character_count] == '*' and linesWithoutSpace[character_count+1] == '/':
                    character_count = character_count + 2
                    break
                if linesWithoutSpace[character_count] == '\n':
                    code_only_lines = code_only_lines + linesWithoutSpace[character_count]
                character_count = character_count + 1
        elif character_count + 1 < code_length and linesWithoutSpace[character_count] == '@' and linesWithoutSpace[character_count + 1] == '"':
            code_only_lines = code_only_lines + linesWithoutSpace[character_count]
            code_only_lines = code_only_lines + linesWithoutSpace[character_count+1]
            character_count = character_count + 2
            while character_count < code_length:
                if character_count + 1 < code_length and linesWithoutSpace[character_count] == '\"':
                    code_only_lines = code_only_lines + linesWithoutSpace[character_count]
                    character_count = character_count + 1
                    break
                elif linesWithoutSpace[character_count] == '\n':
                    code_only_lines =  code_only_lines + "temp\n" + linesWithoutSpace[character_count]
                else:
                    code_only_lines = code_only_lines + linesWithoutSpace[character_count]
                character_count = character_count + 1
        else:
            code_only_lines = code_only_lines + linesWithoutSpace[character_count]
            character_count = character_count + 1

    code_only_inline = code_only_lines.splitlines()
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
    print("numner of code", count_code_line)