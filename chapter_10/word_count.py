def count_words(filename):
    """count the approx number of words in the file."""
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


filename = 'alice.txt'
count_words(filename)

print()


filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'siddhartha.txt']
for filename in filenames:
    count_words(filename)

