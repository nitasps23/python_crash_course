# Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")  # Doing Something After a for Loop


# Avoiding Indentation Errors

# Forgetting to Indent
# Forgetting to Indent Additional Lines  = logical error

for magician in magicians:        
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Indenting Unnecessarily After the Loop

# logical error
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")  # Doing Something After a for Loop

# Forgetting the Colon

magicians = ['alice', 'david', 'carolina']
#for magician in magicians   < --- error :
    #print(magician)