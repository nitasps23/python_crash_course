# reading an entire file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip()) # remove the blank line at the end of file

print()

# file path
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip()) # remove the blank line at the end of file

print()

# absolute file path
file_path = '/Users/nitasps23/Documents/coding_temple/python/python_crash_course/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip()) # remove the blank line at the end of file

print()

# reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())



