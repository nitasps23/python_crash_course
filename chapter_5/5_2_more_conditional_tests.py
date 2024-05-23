# More Conditional Tests:

# You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:


# Tests for equality and inequality with strings

date = 5

if date == 5:
    print(f'{date}th is my birth date!')

date = 6

if date != 5:
    print('That is not my birth date!')

# Tests using the lower() function

usernames = ['NITA023', 'NTSP52', 'NITA23', 'BLOCLA09']

print("\nThese are usernames on the list: ")

for username in usernames:
    if username == username.upper():
        print(username.lower())
    else:
        print(username)


# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again")

print("\nHow old am I?")

age = 39

if age == 38:
    print(f"Yes! I am {age}.")
else:
    print("That's not my age. Try again.")

# inequality

print("\nYour today rewards: ")

reward = 5

if reward != 0:
    print(f"Congrats! You earned {reward} points today!")
else:
    print("Sorry! No reward for you today..")


# greater than

print("\nCheck your score: ")
score = 54

if score > 50:
    print(f"Congrats! Your score is {score}. You passed the test!")
else:
    print(f"Sorry! Your score is {score}. You did't pass this time..")


# less than

print("\nCheck your score: ")
score = 32

if score < 50:
    print(f"Sorry! Your score is {score}. You did't pass this time..")
else:
    print(f"Congrats! Your score is {score}. You passed the test!")

# greater than or equal to

print("\nCheck your score: ")
score = 50

if score >= 50:
    print(f"Congrats! Your score is {score}. You passed the test!")
else:
    print(f"Sorry! Your score is {score}. You did't pass this time..")

# less than or equal to

print("\nCheck your score: ")
score = 50

if score <= 50:
    print(f"Sorry! Your score is {score}. You did't pass this time..")
else:
    print(f"Congrats! Your score is {score}. You passed the test!")



# Tests using the and keyword and the or keyword

my_score = 89
my_friend_score = 23

print("\nDid both of us pass the test? " + str((my_score >= 50) and (my_friend_score >=50)) )
print("Did one of us pass the test? " + str((my_score >= 50) or (my_friend_score >=50)) )


# Test whether an item is in a list

items = ['phone', 'clothes', 'books', 'wallet']

print('phone' in items)
print('phone' not in items)     # Test whether an item is not in a list

