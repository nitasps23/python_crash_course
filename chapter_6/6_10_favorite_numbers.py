# Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers

favorite_numbers = {}

favorite_numbers['laura'] = [5, 34]
favorite_numbers['ae'] = [17, 7]
favorite_numbers['mom'] = [6, 9]
favorite_numbers['dad'] = [29, 6, 5]
favorite_numbers['suriya'] = [10, 12]

print(favorite_numbers)

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")