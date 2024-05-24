# Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

rivers = {}

rivers['nile'] = 'egypt'
rivers['amazon'] = 'brazil'
rivers['yangtze'] = 'china'

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# • Use a loop to print the name of each river included in the dictionary.

print("\nName of the rivers:\n")

for river in sorted(rivers.keys()):
    print(f"\t{river.title()}")

# • Use a loop to print the name of each country included in the dictionary.

print("\nName of the countries:\n")

for country in sorted(rivers.values()):
    print(f"\t{country.title()}")