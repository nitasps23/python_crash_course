# Tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


# dimensions[0] = 250       <--- doesn't work


# Looping Through All Values in a Tuple

for dimension in dimensions:
    print(dimension)

# Writing over a Tuple

# you can’t modify a tuple, you can assign a new value to a variable that holds a tuple

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)