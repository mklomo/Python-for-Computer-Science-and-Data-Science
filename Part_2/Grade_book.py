""" Using a dictionary to represent an insructor's grade book """

# Initialization Phase

grade_book = {
    "Susan" : [90, 76, 94, 87] ,
    "Eduardo" : [83, 98, 87, 78] ,
    "Maame" : [75, 76, 98, 88] ,
    "Pantipa" : [77, 88, 82, 93]
}


# Processing Phase

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f"Average for {name} is {total/len(grades):.2f}")
    all_grades_total += total
    all_grades_count += len(grades)


# Termination Phase

print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")
