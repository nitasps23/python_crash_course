# fileNotFound error

filename = 'alice2.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
else:
    # count the approx number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

print()

# analyzing text
title = "Alice in Wonderland"
print(title.split())

print()


print("# failing silently")

filename = 'alice2.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    # count the approx number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

