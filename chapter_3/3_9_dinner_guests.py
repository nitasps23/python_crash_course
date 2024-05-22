# Working with one of the programs from Exercises 3-4 through 3-7 (page 46), 
# use len() to print a message indicating the number of people you are inviting to dinner

guest_list = ['eleanor roosevelt', 'alicia keys', 'lionel messi']
cancelled_guest = 'eleanor roosevelt'
guest_list.remove(cancelled_guest)
guest_list.insert(0, 'amelia earhart')
guest_list.insert(0, 'beyonce')
guest_list.insert(2, 'barack obama')
guest_list.append('michelle obama')

print(guest_list)

print("Total number of guests we are inviting to dinner: " + str(len(guest_list)) + " people")

