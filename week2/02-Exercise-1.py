import sys
import argparse

# Simply prints the content of the file to the console
def print_file_content(file):
    for line in file:
        print(line.rstrip())

# Writes a list of strings to the output_file.
def write_list_to_file(output_file,lst):
    with open(output_file, "w") as file_object:
        for line in lst:
            file_object.write(line)

# Reads an entire file to a list of strings.
def read_file(input_file):
    with open(input_file) as file_object:
        contents = file_object.readlines()
        return(contents)

# Sets up the argument parser
def parser_setup():
    parser = argparse.ArgumentParser(description="A Program that reads a file from CLI and writes it to the console and an output-file")
    parser.add_argument('-out', '--output', default="out.txt", help="Name of the file to which the output will be written to.")
    parser.add_argument('-in', '--input', help="Name of the file which should be opend.")
    return(parser.parse_args())

if __name__ == "__main__":
    args = parser_setup()
    
    file = read_file(args.input)
    print_file_content(file)
    write_list_to_file(args.output, file)