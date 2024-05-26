cars = ['audi', 'ferrari', 'ford focus', 'toyota sienna']
groceries = ['grapes', 'oranges', 'bananas' ]

# cars.append('bmw')
# cars.append('honda')
# cars.append('chrysler')

# print(cars)

# ------------- #

# def car_adder(car_to_add):
#     cars.append(car_to_add)

# car_adder('bmw')
# car_adder('honda')
# car_adder('chrysler')

# print(cars)


# ------------- #

def car_adder(car_to_add):
    if car_to_add[0].lower() in 'abcdefg':
        print("This car starts with A-G")
        cars.append(car_to_add)
    else:
        print("This car starts with H-Z and we don't add it to our club")
    for car in cars:
        if len(car) <= 5:
            cars.remove(car)
            print(f"{car} was not added because it is too few characters")

car_adder('bmw')
car_adder('honda')
car_adder('chrysler')
car_adder('Aeep')

print(cars)


# ------------- #


# def car_adder(thing_to_add, target_list):
#     if thing_to_add[0].lower() in 'abcdefg':
#         print("This car starts with A-G")
#         target_list.append(thing_to_add)
#     else:
#         print("This car starts with H-Z and we don't add it to our club")
#     return "yee haw"
#     # for item in target_list:
#     #     if len(item) <= 5:
#     #         target_list.remove(item)
#     #         print(f"{item} was not added because it is too few characters")

# car_adder('bmw', cars)
# car_adder('honda', cars)
# car_adder('cinnamon', groceries)
# car_adder('zapple', groceries)

# print(car_adder("bmw", cars))
# # print(groceries)


# # ------------- #

def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

print(addThree(addTwo(5)))

def namePrinter(first, last, middle=''):
    return f"The name's {last}, {first} {middle} {last}."

# print(namePrinter('james', 'bond', 'freddy'))

# print(addTwo(3))

def giveMeMyGroceries(thing_to_add):
    grocery_list = ['grapes', 'oranges', 'bananas']
    grocery_list.append(thing_to_add)
    return grocery_list


print(giveMeMyGroceries('spaghetti'))


def giveMeMySports(name_to_add):
    sports_dict = {'soccer': ['manchester', 'liverpool', 'bayern'],
                    'basketbell': 'cavaliers',
                    'baseball': 'marlins'}
    sports_dict['wresling'] = name_to_add
    return sports_dict


# print(giveMeMySports('Dan Gable'))

print(giveMeMySports(['Dan Gable', 'the Rock', 'the Undertaker']))