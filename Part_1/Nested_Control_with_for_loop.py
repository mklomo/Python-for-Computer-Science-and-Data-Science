""" Using nested control statements to analyze examination results """

# initialization phase
passes = 0 # number of passes

failures = 0 # number of failures

# Process for ten students

for student in range(10):
    # get one exam result
    result = int(input("Enter result (1=pass, 2=fail): "))

    if result == 1:
        passes += 1

    elif result == 2:
        failures += 1


    else:
        print("Please enter either a 1 or 2")

# termination phase
print("Passed: ", passes)
print("failures: ", failures)

if passes > 8:
    print("Bonus to to instructor")



