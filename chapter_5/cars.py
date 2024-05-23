# Simple Example

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Conditional Tests

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

# case sensitive

car = 'Audi'
print(car == 'audi')

# convert the variable’s value to lowercase before doing the comparison

car = 'Audi'
print(car.lower() == 'audi')

print(car)

