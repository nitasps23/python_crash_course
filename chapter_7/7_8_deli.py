# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwich_orders = ['tuna', 'chicken', 'veggie']

finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()

    print(f"We made your {made_sandwich} sandwich.")
    finished_sandwiches.append(made_sandwich)

print("\nWe made the following sandwiches:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())