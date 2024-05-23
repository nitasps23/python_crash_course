# Start with your program from Exercise 4-1 (page 60). 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

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