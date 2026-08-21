print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The variable name was misspelled as "nmae" instead of "name".
# Solution: Changed "nmae" to "name" so the user's actual name is displayed.
print("Nice to meet you,", name)

age = input("How old are you? ")

# BUG: The program tried to add an integer to the string returned by input().
# Solution: Converted age to an integer before adding 1.
print("Next year you will be", int(age) + 1)