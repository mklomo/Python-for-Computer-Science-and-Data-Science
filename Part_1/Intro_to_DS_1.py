""" This script finds the the max, min and range of three values """


print( "Please enter the numbers at the prompt" )

number_1 = float(input( "Enter the first number: " ))

number_2 = float(input( "Enter the second number: " ))

number_3 = float(input( "Enter the third number: " ))

# Lets find the the minimum

min_number = min(number_1, number_2, number_3)

print("The minimum of the numbers is: ", min_number)


# Lets find the maximum

max_number = max(number_1, number_2, number_3)

print("The maximum of the numbers is: ", max_number)

# Lets find the range too

range_number = max_number - min_number

print("The range of the numbers are: ", range_number)


