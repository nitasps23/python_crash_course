from car import Car

my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# modify an attribut's value
my_car.odometer_reading = 23
my_car.read_odometer()

my_car.update_odormeter(25)
my_car.read_odometer()

my_car.update_odormeter(250)
my_car.read_odometer()

my_car.update_odormeter(20)
my_car.read_odometer()

print("\n# My used car:\n")

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odormeter(23500)
my_used_car.read_odometer()

my_used_car.increment_odormeter(100)
my_used_car.read_odometer()

print()

my_car = Car('ford', 'mustang', 2024)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
