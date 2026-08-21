# Ask the user to enter their full name.
full_name = input("Enter your full name: ")

# Split the full name into individual words.
names = full_name.split()

# Get the first name from the list.
first = names[0]

# Check if the user entered at least two names.
if len(names) >= 2:
    print("Good morning:", first)

# Ask the user to enter their full name again if only one name was provided.
if len(names) == 1:
    full_name = input("Please write your full name: ")