# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods = my_foods  <--- this doesn't work

my_foods.append('cannoli')
friend_foods.append('ice cream')


print("My favourite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

