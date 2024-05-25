# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter pizza toppings you'd like to add to your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"I'll add {toppings} to your pizza.")