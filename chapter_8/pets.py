# Passing Arguments

# Positional Arguments
#function tells us what kind of animal each pet is and the pet’s name

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')       # Multiple Function Calls

describe_pet('harry', 'hamster')    # Order Matters in Positional Arguments


# Keyword Arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type= 'hamster', pet_name= 'harry')

describe_pet(pet_name= 'harry', animal_type= 'hamster')


# Default Values

def describe_pet(pet_name, animal_type= 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

describe_pet('willie')

describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Avoiding Argument Errors

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet()    <-- error

