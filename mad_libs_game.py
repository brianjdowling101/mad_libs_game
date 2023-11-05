# string concatenation (aka: how to put a string together)

# Display the title of the story
print("Title: The Adventure at Hogwarts")

# Prompt the user for their name and store it in the 'Name' variable
Name = input("Name: ")

# Prompt the user for a magical creature and store it in the 'magical_creature' variable
magical_creature = input("Magical Creature: ")

# Prompt the user for an adjective and store it in the 'adj' variable
adj = input("Adjective: ")

# Prompt the user for a noun and store it in the 'noun1' variable
noun1 = input("Noun: ")

# Create the madlib story using f-strings, incorporating the user's inputs
madlib = f"Once upon a time in the magical world of Hogwarts, " \
         f"a young wizard named {Name} received an acceptance letter to attend " \
         f"the prestigious Hogwarts School of Witchcraft and Wizardry. " \
         f"{Name} was thrilled and packed their bags with {adj} robes, " \
         f"{noun1}, and a trusty {magical_creature} for companionship."

# Display the generated madlib story
print(madlib)
