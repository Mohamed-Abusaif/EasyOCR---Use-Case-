import os
import time

INPUT_DIR = 'input/'

def is_normal_filename(filename):
    first_char = filename[0]
    # Check if the first character is alphanumeric
    return first_char.isalnum()

# Function to check if filename length is less than or equal to 25 characters
def is_valid_filename_length(filename):
    return len(filename) <= 25

# Function to check if file modification date is before a specified year 
def is_modified_before_year(file_path, year):
    modification_time = os.path.getmtime(file_path)
    modification_date = time.localtime(modification_time)
    return modification_date.tm_year < year

DELETE_BEFORE_YEAR = 2020

# loop over files in the input directory
for filename in os.listdir(INPUT_DIR):
    file_path = os.path.join(INPUT_DIR, filename)

    if (not is_normal_filename(filename) or 
        not is_valid_filename_length(filename) or 
        is_modified_before_year(file_path, DELETE_BEFORE_YEAR)):
        # Delete the file
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    else:
        print(f"File is normal: {file_path}")
