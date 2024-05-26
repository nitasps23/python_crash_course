# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

def make_shirt(size, text):
    """Display information of size and message of the shirt"""
    print(f"\nShirt size is {size} and print \"{text}\" on it.")

