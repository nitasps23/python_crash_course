# my_input = input("what's your input ")
# print(my_input)

#======#

# x = 0

# flag = True

# while flag:
#     print(x)
#     x += 1
#     if x > 100:
#         flag = False


#------#

# x = 0

# flag = True

# while flag:
#     pass


#======#

while True:
    my_name = input("what's your name?\n")

    if my_name.lower() == 'quit':
        break
    elif my_name.lower()[0] in 'abcdefg':
        print('please go to table one')
    elif my_name.lower()[0] in 'hijklmnop':
        print('please go to table two')
    elif my_name.lower()[0] in 'qrstuvwxyz':
        print('please go to table three')


# for letter in 'yee haw':
#     print(letter)