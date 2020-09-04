import sys
import argparse

# Simply prints the content of the file to the console
def print_file_content(file):
    for line in file:
        print(line.rstrip())

def helper(output_file, *lines):
    with open(output_file, "w") as file_object:
        for line in lines:
            if type(line) is list:
                for element in line:
                    if not element.endswith("\n"):
                        file_object.write(element + "\n")
                    else:
                        file_object.write(element)
            else:
                file_object.write(line)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Program that reads a file from CLI and writes it to the console and an output-file")
    parser.add_argument('--output',help="Name of the file to which the output will be written to.")
    parser.add_argument('--file', default="input.txt", help="Name of the file which should be opend.")
    args, unknown = parser.parse_known_args()
    file = read_file(args.file)
    if(args.output == None):
        print_file_content(file)
        for element in unknown:
            print(element + "\n")
    else:
        helper(args.output, file, unknown)