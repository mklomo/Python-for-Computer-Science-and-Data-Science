# Divide_By_Zero


""" Simple exception handling """

while True:
    # Attempt to convert and divide values

    try:
        number_1 = int(input("Enter numerator: "))

        number_2 = int(input("Enter denominator: "))

        result = number_1 / number_2


        # Try to convert non-numeric value to int
    except ValueError:      
        print("You must enter two integers \n")

        # Denominator was 0
    except ZeroDivisionError:         
        print("Attempted to divide by zero \n")

        # executes if no exceptions occur
    else:   
        print(f"{number_1:.3f} / {number_2:.3f} = {result:.3f}")

        break   # Terminate loop

