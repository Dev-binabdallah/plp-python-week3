age = int(input("Enter your age: "))
is_adult = age >= 18
print(is_adult)
if is_adult == True:
    print("You are an adult, pay the full ticket price of Ksh.200")
else:
    print("You are a child pay Ksh. 100 ticket price")