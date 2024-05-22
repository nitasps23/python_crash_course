print("radicals :)\n")
print(" ")
print("\tmore cool code stuff!")

#help(str)

my_str = "hello mr bean"

print(my_str.title())

my_list = [1, 2, 3, 4, 5]

print(my_list)

print(type(my_list))

print(my_list[2])

print(len(my_list))

my_list = [1, 2, 99999, "apple", 5, False, [2, 3, 4]]

zebra = 'stripes'

a = my_list[0]
b = my_list[4]
c = my_list[6][1]

my_list[4] = zebra

print(a)
print(b)
print(c)

my_list[6].append('bike tire')

print(my_list)


my_list.insert(1, "tangerines")

print(my_list)

my_list.remove(2)

print(my_list)

my_list = [1, 2, 2, 99999, "apple", 5, False, [2, 3, 4]]

my_list.remove(2)
my_list.remove(2)

del my_list[0]

print(my_list)


my_list = [1, 2, 99999, 5, 8]

#ordered_list = my_list.sort()

print(sorted(my_list))
print(my_list)

my_list.sort()

print(my_list)



my_list = [1, 2, 99999, 5, 8]

my_list.reverse()
print(my_list)