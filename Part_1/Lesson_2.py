""" Compare integers using if statements and comparison operators. """

print("Enter two numbers and I will tell you", 
"the relationships they satisfy")


# Let the user enter their two numbers

value_1 = float(input("Enter your first number: "))

value_2 = float(input("Enter your second number: "))


# Lets use our relational operators

if value_1 > value_2:
    print(value_1, " is greater than ", value_2)

elif value_1 == value_2:
    print(value_1, " is equal to ", value_2)

else:
    print(value_2, " is greater than ", value_1)

