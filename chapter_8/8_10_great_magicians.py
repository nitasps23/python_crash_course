# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.


def show_magicians(magicians):
    """Print the name of magician in the list."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add the phrase the Great to each magician's name."""
    great_magicians = []

    while magicians:
        great_magician = magicians.pop()
        great_magician = great_magician + " the great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magician_list = ['harry houdini', 'david blaine', 'david copperfield', 'criss angel']
print("Here is a list of magicians:\n")
show_magicians(magician_list)

print(" ")
make_great(magician_list)
show_magicians(magician_list)