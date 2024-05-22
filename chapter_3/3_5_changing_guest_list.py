# You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. 
# Add a print statement at the end of your program stating the name of the guest who can’t make it.

guest_list = ['eleanor roosevelt', 'alicia keys', 'lionel messi']
message = " Come over for dinner, and let's make some new memories together."

cancelled_guest = 'eleanor roosevelt'
guest_list.remove(cancelled_guest)
print("Guest(s) who cannot make it to dinner: " + "\n\t" + cancelled_guest.title())

## Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

print(guest_list)

guest_list.insert(0, 'amelia earhart')
print(guest_list)


### Print a second set of invitation messages, one for each person who is still in your list.

print("Greeting " + guest_list[0].title() + "!" + message)
print("Greeting " + guest_list[1].title() + "!" + message)
print("Greeting " + guest_list[-1].title() + "!" + message)