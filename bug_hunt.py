#BUG: The print statement missed closing qoute, so added one.
print("Welcome to the Bug Hunt!")
name = input("What is your name? ")
print("Nice to meet you, nmae")
age = input("How old are you? ")
#BUG: The print statement cancatenated a string (age) with integer (1).
#BUG: Used (+) to cancatenate a qouted string with integer
      #solution: converted age to integer and used coma to seperate the age from the statement "Next year you will be" and the (+) sign.
print("Next year you will be", int(age) + 1)
