# Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    'new york': {
        'country': 'usa',
        'population': 8.46,
        'fact': 'the city that never sleeps',
        },
    'paris': {
        'country': 'france',
        'population': 2.16,
        'fact': 'the city of love',
        },
    'london': {
        'country': 'uk',
        'population': 8.98,
        'fact': 'the square mile',
        }
    }

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")

    if city_info['country'] == 'usa' or city_info['country'] == 'uk':
        print(f"\tCountry: {city_info['country'].upper()}")
    else:
        print(f"\tCountry: {city_info['country'].title()}")

    print(f"\tPopulation: {city_info['population']} million")
    print(f"\tFact: Also known as \"{city_info['fact'].capitalize()}\"")