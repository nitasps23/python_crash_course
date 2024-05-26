# Defining a Function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing Information to a Function

# adding username here you allow the function 
# to accept any value of username you specify.

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')


# Using a Function with a while Loop

# use the get_formatted_name() function with a while
# loop to greet users more formally

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

# This is an infinite loop!

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':   # break statement offers a straightforward 
        break           # way to exit the loop at either prompt
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

