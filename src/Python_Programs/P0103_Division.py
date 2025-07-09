# Division
try:
    num3 = float(input("Enter the numerator:  "))
    num4 = float(input("Enter the denominator:  "))

    if num4 == 0:
        print("Error: Division by zero is not allowed.")
    else: 
        div_result = num3 / num4
        print(f"Division: {num3} / {num4} = {div_result:.2f}")
except ValueError:
    print("Error: Please enter valid numbers.")
