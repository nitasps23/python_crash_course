# Removing All Instances of Specific Values from a List

# remove 'cat' from a list of pets with the value 'cat' repeated several times

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)