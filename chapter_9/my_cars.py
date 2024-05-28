# import multiple classes from a module

# from car import Car, ElectricCar



# import an entire module

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# import all classes from a module
# NOT RECOMMENDED
from car import *


# importing a module in a module

from car import Car
from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print()

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print()
