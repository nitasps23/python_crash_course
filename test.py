def add_length(str_):
    #your code here
    str_ = str_.split()
    w_list = []

    for word in str_:
        w_list.append(word + " " + str(len(word)))
    return w_list


string = "You will win"

print(add_length(string))


my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', 'Remove','Keep', 'Remove','Keep', 'Remove']

new_list = my_list[::2]

print(new_list)


def myFunc(list):
    return list[::2]


print(myFunc(my_list))