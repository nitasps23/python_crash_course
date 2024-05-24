# Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

tammy = {'kind': 'dog', 'owner': 'nita'}
izzy = {'kind': 'dog', 'owner': 'laura'}
frankie = {'kind': 'dog', 'owner': 'kaitlyn'}
emma = {'kind': 'cat', 'owner': 'wilson'}

pets = [tammy, izzy, frankie, emma]

for pet in pets:
    print(pet)