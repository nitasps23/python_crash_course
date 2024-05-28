"""A class that can be used to represent a car."""

class Car():
    """a simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attribute to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odormeter(self, mileage):
        """
        Setting the odometer reading to the giving value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odormeter(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("This car needs Premium 91!")
    
