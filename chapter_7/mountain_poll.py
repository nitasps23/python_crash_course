# Filling a Dictionary with User Input

# a polling program in which each pass through the loop
# prompts for the participant’s name and response

responses = {}

# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")   # Prompt for the person's name and response.
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response      # Store the response in the dictionary.

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ") 
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")





