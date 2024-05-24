# # Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

laura_info = {}

laura_info['first_name'] = 'laura'
laura_info['last_name'] = 'block'
laura_info['age'] = 35
laura_info['city'] = 'new york'

# print(laura_info)

nita_info = {}

nita_info['first_name'] = 'nita'
nita_info['last_name'] = 'sokphoodsa'
nita_info['age'] = 38
nita_info['city'] = 'queens'

# print(nita_info)

ae_info = {}

ae_info['first_name'] = 'dhitikarn'
ae_info['last_name'] = 'rojanawongsri'
ae_info['age'] = 37
ae_info['city'] = 'queens'

# print(ae_info)

people = [laura_info, nita_info, ae_info]

for person in people:
    print(person)