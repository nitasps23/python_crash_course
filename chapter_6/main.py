print(5 == 5)

x = 5
y = 6

if x != 5 or y == 5:
    print("panang curry")
# elif x != 5 or y == 6:
#     print("thai food")
elif x == 6 and y == 5:
    print("yee haw")


# ---------- #

x = []
y = "elephant ate a LOT"

if x:
    print("howdy")
elif y:
    print("hello from here")

# ---------- #

# loops
# dictionaries

my_dict = {
    'key': 'value',
    1: 'spaghetti',
    2: 'pasta',
    3: 'pizza',
    'cats': 'no thanks',
    10.5: 4
}

print(my_dict[10.5])

print(my_dict)

my_dict['new key'] = 'alpha'

print(my_dict)

my_dict[2] = 'cheesy bread'
my_dict[2] = 'endless bread'

print(my_dict)

# ---------- #

del my_dict[2]
my_dict[2] = ''

print(my_dict)

x = my_dict.get(3)
print(x)

# ---------- #

my_dict = {
    'key': 'value',
    1: 'spaghetti',
    2: 'pasta',
    3: 'pizza',
    'cats': 'no thanks',
    10.5: 4
}

my_dict['new key'] = 'alpha'
my_dict[2] = 'cheesy bread'
my_dict[2] = 'endless bread'

for key, value in my_dict.items():
    print(f"The key is {key}")
    print(f"And this is the value: {value}")


# ---------- #

my_dict = {
    'key': 'value',
    1: 'spaghetti',
    2: 'pasta',
    3: 'pizza',
    'cats': 'no thanks',
    10.5: 4
}

my_dict['new key'] = 'alpha'
my_dict[2] = 'cheesy bread'
my_dict[2] = 'endless bread'


for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)


# ---------- #

my_dict = {
    'key': 'value',
    1: 'spaghetti',
    2: 'pasta',
    3: 'pizza',
    'cats': 'no thanks',
    10.5: 4
}

my_dict['new key'] = 'alpha'
my_dict[2] = 'cheesy bread'
my_dict[2] = 'endless bread'

for k, v in my_dict.items():
    print(f"The key is {k}")
    print(f"And this is the value: {v}")


# ---------- #

my_dict = {
    'soccer': ['Manchester City', 'Bayern', 'Seattle Sounders'],
    'formula one': {'driver': 'andretti'},
    'football': {'nfl': ['seahawks', 'packers', 'NOT THE PATRIOTS'],
                 'college': ['Clemson', 'UCLA', 'ANYONE BUT ALABAMA'],
                 1: 3}
}

print(isinstance(my_dict['football']['college'], list))

print(isinstance('Hello', str))