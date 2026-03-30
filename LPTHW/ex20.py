# Imports argv from the sys module to access command-line arguments.
from sys import argv
# Assigning arguments
script, input_file = argv
# Defines a function print_all, which reads the contents of a file object f and prints it.
def print_all(f):
    print(f.read())
# Defines a function that moves the file pointer back to the beginning of the file.
def rewind(f):
    f.seek(0)
# Defines a function that prints a line number and the next line read from the file.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Opens the file specified by input_file and stores the file object in current_file.
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:\n")
# Selecting the beginning of the file and printing the first line
current_line = 1
print_a_line(current_line, current_file)
# Selecting the second line printing it
current_line += 1
print_a_line(current_line, current_file)
# Selecting the third line and printing it
current_line += 1
print_a_line(current_line, current_file)