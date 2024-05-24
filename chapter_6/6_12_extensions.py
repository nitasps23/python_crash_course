
# We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

tammy = {'kind': 'dog', 'owner': 'nita'}
izzy = {'kind': 'dog', 'owner': 'laura'}
frankie = {'kind': 'dog', 'owner': 'kaitlyn'}
emma = {'kind': 'cat', 'owner': 'wilson'}

pets = [tammy, izzy, frankie, emma]

for pet in pets:
    print(pet)


# extensions

pets = {
    'tammy': {
        'kind': 'dog',
        'age': 12,
        'owner': 'nita',
        },
    'izzy': {
        'kind': 'dog',
        'age': 13,
        'owner': 'laura',
        },
    'frankie': {
        'kind': 'dog',
        'age': 10,
        'owner': 'kaitlyn',
        },
    'emma': {
        'kind': 'cat',
        'age': 4,
        'owner': 'Wilson',
        }
    }

for pet, pet_info in pets.items():
    print(f"\nPet Name: {pet.title()}")

    print(f"\tKind of animal: {pet_info['kind'].title()}")
    print(f"\tAge: {pet_info['age']} years old")
    print(f"\tOwner's Name: {pet_info['owner'].title()}")