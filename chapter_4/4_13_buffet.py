# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

foods = ('pizza', 'sandwich', 'burger', 'hot dog', 'fries')


# Use a for loop to print each food the restaurant offers.

print("\nBuffet-style restaurant's food options: ")
for food in foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.

# foods[0] = "steak"  <----- REJECTED

# The restaurant changes its menu, replacing two of the items with different foods. 
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

print("\nOriginal food options:")
for food in foods:
    print(food)

foods = ('steak', 'sandwich', 'burger', 'hot dog', 'wings')

print("\nRevised food options:")
for food in foods:
    print(food)

    