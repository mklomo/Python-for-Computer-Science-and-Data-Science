""" This is a script that summarizes the results if students using nested control and sentinel loops """

# Lets initialize
pass_grade_counter = 0

fail_grade_counter = 0

grade = int(input("Please enter the grade of the student (i.e. a 1 or a 2 or a 0 to end): "))


# Processing phase
while grade != 0:
    if grade == 1:
        pass_grade_counter += 1


    elif grade == 2:
        fail_grade_counter += 1
    
    elif grade != 1 or 2:
        print("wrong entry please enter a 1 or 2\n")

    grade = int(input("Please enter the grade of the student (i.e. a 1 or a 2 or a 0 to end): "))


# Termination Phase

# Displaying results summary


if pass_grade_counter >= 8:
    print(f'The number of students who passed the exam is {pass_grade_counter} and {fail_grade_counter} students failed the exams. Bonus to instructor!!')


else:
    print(f'The number of students who passed the exam is {pass_grade_counter} and {fail_grade_counter} students failed the exams.')