# Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8

# Use four spaces for each indentation level. 
# Set your text editor to insert four spaces every time you press tab, 
# if you haven’t already done so (see Appendix B for instructions on how to do this).

# Use less than 80 characters on each line, and set your editor to show a
# vertical guideline at the 80th character position.

# Don’t use blank lines excessively in your program files.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are: ")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are: ")
for food in friend_foods:
    print(food)

print(" ")

animals = ['dolphin', 'whale', 'shark']

for animal in animals:
    print(animal)


# Modify your program to print a statement about each animal, such as A dog would make a great pet.

for animal in animals:
    print("When I go diving, I want to see a " + animal + ".\n")

# Add a line at the end of your program stating what these animals have in common. 
# You could print a sentence such as Any of these animals would make a great pet!

for animal in animals:
    print("When I go diving, I want to see a " + animal + ".\n")

print("It would be awesome to see any of these animals!")

pizzas = ['cheese', 'pepperoni', 'hawaiian']

friend_pizzas =pizzas[:]

# Add a new pizza to the original list.

pizzas.append('veggie')

# Add a different pizza to the list friend_pizzas.

friend_pizzas.append('margherita')

# Prove that you have two separate lists. Print the message, My favorite pizzas are:, 
# and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print(" ")

print("My favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza)

print(" ")

print("My friend’s favorite pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza)