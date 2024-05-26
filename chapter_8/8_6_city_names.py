# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.

def city_country(city_name, country_name):
    """Return the formatted name of a city and its country."""
    if country_name == 'USA':
        city_info = city_name.title() + ", " + country_name.upper()
    else:
        city_info = city_name.title() + ", " + country_name.title()
    
    return city_info

city = city_country('paris', 'france')
print(city)

city = city_country('new york', 'USA')
print(city)

city = city_country('bangkok', 'thailand')
print(city)