class Dog():
    """ a simple attempt to model a dog. """

    def __init__(self, name, age):
        """initialize name and get attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

             
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()


print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()