# Writing Clear Prompts

name = input("Please enter your name: ")
print(f"Hello, {name}!")


# store your prompt in a variable and pass that variable to the input()
# function. This allows you to build your prompt over several lines

prompt = "If you tell me who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"Hello, {name}!")


# Using int() to Accept Numerical Input

age = input("How old are you? ")

age = int(age)
age >= 18

