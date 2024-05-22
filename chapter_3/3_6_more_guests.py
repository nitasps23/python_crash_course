# More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print statement to the end of your program informing people that you found a bigger dinner table.

guest_list = ['eleanor roosevelt', 'alicia keys', 'lionel messi']
cancelled_guest = 'eleanor roosevelt'
guest_list.remove(cancelled_guest)
guest_list.insert(0, 'amelia earhart')
print(guest_list)

message = " Come over for dinner, and let's make some new memories together."
message_2 = " We would like to inform you that we found a bigger dinner table and will be having more guests joining us!"

print("Greeting " + guest_list[0].title() + "!" + message_2)
print("Greeting " + guest_list[1].title() + "!" + message_2)
print("Greeting " + guest_list[-1].title() + "!" + message_2)

# Use insert() to add one new guest to the beginning of your list.

guest_list.insert(0, 'beyonce')
print(guest_list)

# Use insert() to add one new guest to the middle of your list.

guest_list.insert(2, 'barack obama')
print(guest_list)

# Use append() to add one new guest to the end of your list.

guest_list.append('michelle obama')
print(guest_list)

# Print a new set of invitation messages, one for each person in your list.

print("Greeting " + guest_list[0].title() + "!" + message)
print("Greeting " + guest_list[1].title() + "!" + message)
print("Greeting " + guest_list[2].title() + "!" + message)
print("Greeting " + guest_list[3].title() + "!" + message)
print("Greeting " + guest_list[4].title() + "!" + message)
print("Greeting " + guest_list[5].title() + "!" + message)