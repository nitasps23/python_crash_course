# Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


# list of wine in stock today

wine_list = ['metlot', 'cab franc', 'prosecco', 'rose', ]
print(wine_list)

# Accessing Elements in a List

print("\n" + wine_list[0].title())
print(wine_list[1].title())
print(wine_list[2].title())
print(wine_list[-1].title())

# Using Individual Values from a List

message = "\nOur today bestseller: " + wine_list[1].title() + "!"
message_1 = "\nOur today staff pick: " + wine_list[-1].title() + "!"

print(message)
print(message_1)

# Changing, Adding, and Removing Elements

print("\n")
print(wine_list)

wine_list[0] = 'cab sauvignon'      # replacing wine on the list

print(wine_list)

# adding more wine selection

wine_list.append('chardonnay')
wine_list.append('chenin blanc')

print(wine_list)

# inserting

wine_list.insert(0, 'syrah')

print(wine_list)

# removing del 

del wine_list[-1]       # remove chenin blanc from list
print(wine_list)

# removing pop

poped_wine_list = wine_list.pop()
print(wine_list)
print(poped_wine_list)

last_added = wine_list.pop()    # use the pop() method to print a statement about the last motorcycle
print("\nThe last wine added to the list was " + last_added.title() + ".")

# use pop() to remove an item in a list at any position

first_added = wine_list.pop(0)
print("The first wine added to the list was " + first_added.title() + ".")

# removing by value (remove)

print("\n")
print(wine_list)

wine_list.remove('prosecco')
print(wine_list)

most_pick = 'cab franc'
wine_list.remove(most_pick)
print(wine_list)
print("\n" + most_pick.title() + " is the most pick wine of the month!")


# Organizing a List

# Sorting a List Permanently with the sort() Method

print("\n")
wine_list.append('syrah')       # add more wine selections
wine_list.append('cab franc')
wine_list.append('prosecco')
wine_list.append('rose')

print(wine_list)

wine_list.sort()
print(wine_list)

wine_list.sort(reverse= True)
print(wine_list)


# maintain the original order of a list

wine_list = ['cab sauvignon', 'syrah', 'cab franc', 'prosecco', 'rose']

print("\nHere is the original list: ")
print(wine_list)

print("\nHere is the sorted list: ")
print(sorted(wine_list))

print("\nHere is the original list again: ")
print(wine_list)

# Printing a List in Reverse Order

wine_list.reverse()
print(wine_list)

# Finding the Length of a List

print(len(wine_list))