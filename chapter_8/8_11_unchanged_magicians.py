# Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.


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

    return magicians

magician_list = ['harry houdini', 'david blaine', 'david copperfield', 'criss angel']
print("Here is a list of magicians:\n")
show_magicians(magician_list)

print("\nHere is a list of the Great magicians:\n")
great_magicians = make_great(magician_list[:])
show_magicians(great_magicians)

print("\nHere is the orignal list of magicians:\n")
show_magicians(magician_list)