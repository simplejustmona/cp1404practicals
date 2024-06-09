"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
#Q1 A ValueError will occur if the user inputs a value that cannot be converted to an integer.
#Q2 A ZeroDivisionError will occur if the user enters a denominator of 0. Division by zero is mathematically undefined.
#Q3 Yes, to avoid the possibility of a ZeroDivisionError, we can include a conditional check to ensure that the denominator is not equal to 0 before performing the division operation. We can do this by adding an if statement before the division operation.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
