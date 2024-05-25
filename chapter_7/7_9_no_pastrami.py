# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'veggie', 'pastrami']

finished_sandwiches = []

print("Our deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()

    print(f"We made your {made_sandwich} sandwich.")
    finished_sandwiches.append(made_sandwich)

print("\nWe made the following sandwiches:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())