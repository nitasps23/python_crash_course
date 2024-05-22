# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.

locations = ['italy', 'sahara', 'annecy', 'banff', 'iceland']

# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

print(locations)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print("\nHere is the sorted list: ")
print(sorted(locations))

# Show that your list is still in its original order by printing it.

print("\nHere is the original list: ")
print(locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

print("\nHere is the sorted list in reverse: ")
print(sorted(locations, reverse= True))

# Show that your list is still in its original order by printing it again.

print("\nHere is the original list: ")
print(locations)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.

locations.reverse()
print(locations)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

locations.reverse()
print(locations)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

locations.sort()
print(locations)

# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

locations.sort(reverse= True)
print(locations)