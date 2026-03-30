# using argv to get a filename
from sys import argv

script, filename = argv
# opening a filename
txt = open(filename)
# printing the filename
print(f"Here's your file {filename}:")
#showing what's inside of the filename
print(txt.read())

print("Type the filename again:")
#calling the file again:
file_again = input("> ")
#looking what's inside of the filename
txt_again = open(file_again)
#printing what's inside of the filename
print(txt_again.read())

txt = close(filename)
txt_again = close(filename)