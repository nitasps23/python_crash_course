# Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:

# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.


prompt = "\nPlease enter pizza toppings you'd like to add to your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"

active = True

while active:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    elif toppings == "":
        active = False
    else:
        print(f"I'll add {toppings} to your pizza.")