# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich(*sandwiches):
    """Print a summary of a sandwich being ordered."""
    print("\nHere is a summary of your sandwich order:")
    for sandwich in sandwiches:
        print(f"- {sandwich}")

make_sandwich('turkey')
make_sandwich('turkey', 'tomatoes')
make_sandwich('turkey', 'tomatoes', 'pickles', 'cucumber')
