# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
# print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name.

names = ['ae', 'wilson', 'rich']

message = " You are an amazing friend!"

print("Hey " + names[0].title() + "!" + message)
print("Hey " + names[1].title() + "!" + message)
print("Hey " + names[-1].title() + "!" + message)