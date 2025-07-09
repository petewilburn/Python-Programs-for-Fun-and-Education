# Addition
# This program performs addition of two numbers provided by the user.
# Addition

try:
    num1 = float(input("Enter the first number for addition:  "))
    num2 = float(input("Enter the second number for addition:  "))

    sum_result = num1 + num2

    print(f"sum: {num1} + {num2} = {sum_result}")
except ValueError:
    print("Error: Please enter valid numbers.")
