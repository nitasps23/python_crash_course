# Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list

def show_magicians(names):
    """Print the name of magician in the list."""
    for name in names:
        print(name.title())

magician_list = ['harry houdini', 'david blaine', 'david copperfield', 'criss angel']
print("Here is a list of magicians:\n")
show_magicians(magician_list)