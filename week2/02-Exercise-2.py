# This file only tests if it can call the functions in the module 'utils.py'

from modules.utils import *

if __name__ == "__main__":
    # Testing the 1st function
    write_file_names_in_folder_to_file("temp", "dir.txt")
    # Testing the 2nd function
    write_file_names_to_file_recursive("temp","recursive.txt")

    # Testing the 3rd function
    print_first_line(["dir.txt","recursive.txt"])
    # Testing the 3rd function using the output from the 1st function
    correctedNames = ["temp\\"+name for name in get_file_names_in_folder("temp")]
    print_first_line(correctedNames)

    # Testing the 4th function
    print_line_with_email(["emails.txt","emails2.txt","dir.txt"])

    # Testing the 5th function
    write_md_headlines_to_file(["01-Exercise-Solution.ipynb"], "headlines.txt")