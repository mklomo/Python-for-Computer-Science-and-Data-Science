""" This code displays a primitive bar chart """

numbers = [20, 4, 7, 10, 9]


print("\nCreating a bar chart from numbers: ")
print(f"Index{'Value':>8}         Bar")



for index, value in enumerate(numbers):
    print(f"{index:>5}{value:>8}          {'*' * value}")