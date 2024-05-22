# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.

guest_list = ['eleanor roosevelt', 'alicia keys', 'lionel messi']
cancelled_guest = 'eleanor roosevelt'
guest_list.remove(cancelled_guest)
guest_list.insert(0, 'amelia earhart')
guest_list.insert(0, 'beyonce')
guest_list.insert(2, 'barack obama')
guest_list.append('michelle obama')

print(guest_list)

message_3 = " We just heard that the new dinner table won't arrive in time so we can invite only two people for dinner. Our sincere apologies for this change."

print("Greeting " + guest_list[0].title() + "!" + message_3)
print("Greeting " + guest_list[1].title() + "!" + message_3)
print("Greeting " + guest_list[2].title() + "!" + message_3)
print("Greeting " + guest_list[3].title() + "!" + message_3)
print("Greeting " + guest_list[4].title() + "!" + message_3)
print("Greeting " + guest_list[5].title() + "!" + message_3)

# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.

message_4 = " We are sorry to inform you that we can't invite you to dinner."

removed_guest = guest_list.pop(0)
print(guest_list)
print(removed_guest)

print("\nGreeting " + removed_guest.title() + "!" + message_4)

removed_guest = guest_list.pop(0)
print(guest_list)
print(removed_guest)

print("\nGreeting " + removed_guest.title() + "!" + message_4)

removed_guest = guest_list.pop(1)
print(guest_list)
print(removed_guest)

print("\nGreeting " + removed_guest.title() + "!" + message_4)

removed_guest = guest_list.pop(1)
print(guest_list)
print(removed_guest)

print("\nGreeting " + removed_guest.title() + "!" + message_4)

# Print a message to each of the two people still on your list, letting them know they’re still invited.

message_5 = " We are letting you know that you are still invited!"

print(guest_list)

print("Greeting " + guest_list[0].title() + "!" + message_5)
print("Greeting " + guest_list[1].title() + "!" + message_5)

# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

del guest_list[0]
del guest_list[0]

print(guest_list)


