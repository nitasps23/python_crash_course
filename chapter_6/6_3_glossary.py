# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.

# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {}

glossary['variable'] = 'Every variable holds a value, which is the information associated with that variable'
glossary['traceback'] = 'A record of where the interpreter ran into trouble when tryin to execute your code'
glossary['string'] = 'A series of characters'
glossary['concatenation'] = 'A method of combining strings'
glossary['whitespace'] = 'Any nonprinting character such as spaces, tabs, and end-of-line symbols'

print(f"My glossary of programming words:\n")

print(f"\n1) Variable: \n\t{glossary['variable']}.")
print(f"\n2) Traceback: \n\t{glossary['traceback']}.")
print(f"\n3) String: \n\t{glossary['string']}.")
print(f"\n4) Concatenation: \n\t{glossary['concatenation']}.")
print(f"\n5) Whitespace: \n\t{glossary['whitespace']}.")