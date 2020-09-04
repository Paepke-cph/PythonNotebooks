import os

def write_to_file(output_file, fileList):
    with open(output_file, "w") as file_object:
        for file in fileList:
            file_object.write(file + '\n')

# ///////////////////////////////////////////////////////////////////////
# 1st function helper part
def get_file_names_in_folder(folder_name):
    # The check is not very good as file might have the character, but for demonstrating the use of os it seems okay.
    file_list = [name for name in os.listdir(folder_name) if "." in name]
    return(file_list)

# 1st function
def write_file_names_in_folder_to_file(folder_name, output_file):
    file_list = get_file_names_in_folder(folder_name)
    write_to_file(output_file, file_list)

# ///////////////////////////////////////////////////////////////////////
# 2nd function helper part
def recursive_get_file_names(folder_name):
    file_names = []
    for _, _, files in os.walk(folder_name):  
        for filename in files: 
            file_names.append(filename)
    return(file_names)

# 2nd function        
def write_file_names_to_file_recursive(folder_name, output_file):
    file_names = recursive_get_file_names(folder_name)
    write_to_file(output_file, file_names)

# ///////////////////////////////////////////////////////////////////////
# 3rd function
def print_first_line(file_names):
    for name in file_names:
        with open(name) as file:
            print(file.readline())

# ///////////////////////////////////////////////////////////////////////
# 4th function helper part
def get_line_containing(file_names, look_for):
    found = []
    for name in file_names:
        with open(name) as file:
            for line in file.readlines():
                if look_for in line:
                    found.append(line)     
    return(found)

# 4th function
def print_line_with_email(file_names):
    emails = get_line_containing(file_names, "@")
    for email in emails:
        print(email)

# ///////////////////////////////////////////////////////////////////////
# 5th function
def write_md_headlines_to_file(file_names, output_file):
    headlines = get_line_containing(file_names, "#")
    write_to_file(output_file, headlines)

#if  __name__ == "__main__":
#    print("Called as main")
#else:
#    print("Called as module")