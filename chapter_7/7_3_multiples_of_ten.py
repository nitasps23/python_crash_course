# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Give me a number, and I will tell you if it's a multiple of 10 or not: ")

number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")