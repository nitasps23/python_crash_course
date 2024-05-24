# A List of Dictionaries

alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print (alien)

# code that automatically generates each alien

# Make an empty list for storing aliens.

aliens = []

# make 30 green aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

print("...")

# show how many aliens have been created

print(f"Total number of aliens: {len(aliens)}")


# ------------------------ #

### some aliens changing color and moving faster

aliens = []

# make 30 green aliens

for alien_number in range(0,30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10

# show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

print("...")



# ------------------------ #

# adding an elif block that turns yellow aliens into red

aliens = []

# make 30 green aliens

for alien_number in range(0,30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

print("...")