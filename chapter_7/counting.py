# Introducing while Loops

# while loop counts from 1 to 5:

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

# Using continue in a Loop

# use the continue statement to return to the beginning of the
# loop based on the result of a conditional test.

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops

x = 1

while x <= 5:
    print(x)
    x += 1