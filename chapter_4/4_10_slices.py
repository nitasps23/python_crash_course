# Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following:

animals = ['dolphin', 'whale', 'shark']

for animal in animals:
    print(animal)

animals.append('sea turtle')
animals.append('octopus')
animals.append('crab')
animals.append('shrimp')

print(animals)
print(" ")

# Print the message, The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list.

print("The first three items in the list are:\n")

for animal in animals[0:3]:
    print(animal)

# Print the message, Three items from the middle of the list are:. 
# Use a slice to print three items from the middle of the list.

print(" ")

print("Three items from the middle of the list are:\n")

for animal in animals[2:5]:
    print(animal)

# Print the message, The last three items in the list are:. 
# Use a slice to print the last three items in the list.

print(" ")

print("The last three items in the list are:\n")

for animal in animals[-3:]:
    print(animal)


