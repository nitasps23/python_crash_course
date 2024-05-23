# Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.


# If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.

# If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.

# Write one version of this program that runs the if block and another that
# runs the else block.


# if block

alien_color = 'green'

if alien_color == 'green':
    print(f"You just earned 5 points for shooting {alien_color} alien!")
if alien_color == 'yellow' or alien_color == 'red':
    print("You just earned 10 points!")


# else version     

alien_color = 'blue'

if alien_color == 'green':
    print(f"You just earned 5 points for shooting {alien_color} alien!")
else:
    print("You just earned 10 points!")

