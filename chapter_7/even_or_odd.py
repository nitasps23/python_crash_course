# The Modulo Operator

# use this fact to determine
# if a number is even or odd

number = input("Enter a number, and I will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"The number {number} is odd.")

    