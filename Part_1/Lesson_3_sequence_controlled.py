""" A Class Average Program with sequence-controlled repetition """


# Initialization phase

total = 0

grade_counter = 0

grades = [100, 52, 89, 64, 87, 48, 78, 84, 92, 92, 86] # List of grades obtained

for grade in grades:

    total += grade

    grade_counter += 1
    
# Termination phase

average = total / grade_counter

print(f'Class Average is {average}') # An f string enables us to insert values in strings using placeholders