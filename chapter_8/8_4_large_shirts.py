# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size='L', text='I love Python'):
    """Display information of size and message of the shirt"""
    print(f"\nShirt size is {size} and print \"{text}\" on it.")

make_shirt()
make_shirt('M')
make_shirt(size='S', text='Awesome!')