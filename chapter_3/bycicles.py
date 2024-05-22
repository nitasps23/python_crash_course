# list

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List

print(bicycles[0])  #Index Positions Start at 0, Not 1

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])     # last item on the list


# Using Individual Values from a List

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)