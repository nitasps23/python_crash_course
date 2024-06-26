# Checking for Inequality

# store a requested pizza topping in a variable 
# and then print a message if the person did not order anchovies

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!\n")


# Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")


## This code would not work properly if we used an if-elif-else block
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!\n")


# Using if Statements with Lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print (f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


# what if the pizzeria runs out of green peppers? An if statement
# inside the for loop can handle this situation appropriately

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print (f"Adding {requested_topping}.")

print("\nFinished making your pizza!\n")

# Checking That a List Is Not Empty

#check whether the list of requested toppings is
# empty before building the pizza.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print (f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")


# Using Multiple Lists

# watch out for unusual topping requests before we build a pizza

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
