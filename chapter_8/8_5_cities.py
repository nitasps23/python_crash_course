# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city_name, country='USA'):
    """Display information about a city and its country"""
    if country == 'USA':
        print(f"\n{city_name.title()} is in {country}.")
    else:
        print(f"\n{city_name.title()} is in {country.title()}.")

describe_city(city_name='new york')
describe_city(city_name='california')
describe_city(city_name='annecy', country='france')
