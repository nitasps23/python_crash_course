# Changing Case in a String

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Combining or Concatenating Strings

first_name = "ada"
last_name = "lovecase"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title()+ "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

print("Python")
print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace

favorite_language = 'python '
favorite_language

favorite_language.rstrip()
favorite_language

favorite_language = favorite_language.rstrip()
favorite_language

favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

my_string = ".....howdy....."
print(my_string)
print(my_string.lstrip("."))
print(my_string.rstrip("."))
print(my_string.strip("."))

print(my_string)
thing_to_strip = "."
print(my_string.lstrip(thing_to_strip))


# count number of letter
print(message.count("l"))