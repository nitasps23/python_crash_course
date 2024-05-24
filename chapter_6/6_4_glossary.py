# Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {}

glossary['variable'] = 'Every variable holds a value, which is the information associated with that variable'
glossary['traceback'] = 'A record of where the interpreter ran into trouble when tryin to execute your code'
glossary['string'] = 'A series of characters'
glossary['concatenation'] = 'A method of combining strings'
glossary['whitespace'] = 'Any nonprinting character such as spaces, tabs, and end-of-line symbols'

x = 1
counter = x + 1

print("My glossary of programming words:\n")

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}.")


# add 5 more words

glossary['argument'] = 'A value passed to a function (or method) when calling the function'
glossary['dictionary'] = 'An associative array, where arbitrary keys are mapped to values'
glossary['immutable'] = 'An object with a fixed value'
glossary['list'] = 'A built-in Python sequence'
glossary['expression'] = 'A piece of syntax which can be evaluated to some value'

print("\nMy glossary of programming words:\n")

for word, meaning in glossary.items():
    print(f"> {word.title()}: {meaning}.")