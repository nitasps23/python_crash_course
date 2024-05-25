# How the input() Function Works

# asks the user to enter some text,
# then displays that message back to the user

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# while Loops

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


# Using a Flag

# program that should run only as long as many conditions are true.
# the flag is set to True and stop running
# when any of several events sets the value of the flag to False

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)