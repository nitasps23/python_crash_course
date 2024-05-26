# Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section

def display_message():
    """Display message about this chapter"""
    print("I am learning about functions in this chapter!")

display_message()


def favorite_book(title):
    """Display a message about favorite books"""
    print(f"One of my favorite books is {title.title()}")

favorite_book('think and grow rich')


def make_shirt(size='L', text='I love Python'):
    """Display information of size and message of the shirt"""
    print(f"\nShirt size is {size} and print \"{text}\" on it.")

make_shirt()
make_shirt('M')
make_shirt(size='S', text='Awesome!')