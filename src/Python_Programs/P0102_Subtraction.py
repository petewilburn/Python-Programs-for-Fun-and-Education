# This program performs subtraction of two numbers provided by the user.

# ---------------------------------------------------------------------------------------------
# File: P0102_Subtraction.py
# Description: Subtracts the second number from the first number provided by the user.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------
from typing import Union

def subtract_b_from_a(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    Returns the difference of two numbers (a - b).
    Raises ValueError if inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a - b

def print_welcome_message() -> None:
    print("Welcome to the Subtraction Program!")
    print("This program will subtract the second number from the first number.")

def prompt_user_for_numbers() -> tuple[float, float]:
    """Prompts the user for two numbers and returns them as a tuple."""
    count = 0
    while count < 3:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting.")

def print_result(num1: float, num2: float, result: float) -> None:
    """Prints the result of the subtraction."""
    print(f"The difference between {num1} and {num2} is: {result}")

def main() -> None:
    """Main function to execute the subtraction program."""
    print_welcome_message()
    try:
        num1, num2 = prompt_user_for_numbers()
        result = subtract_b_from_a(num1, num2)
        print_result(num1, num2, result)
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for using the Subtraction Program!")
    print("Goodbye!")

if __name__ == "__main__":
    main()

# This code is a simple subtraction program that prompts the user for two numbers,
# subtracts the second number from the first, and prints the result. It includes error handling.
# The program will exit after three invalid attempts to enter numbers.
# It also includes a welcome message and functions to handle the main logic, user input, and result printing.
# The program will input and print the result as float, while the function subtract_b_from_a will take two parameters, 
# a and b, which can be either float or int.
# The function will return the result of subtracting b from a, which can also be either float or int.
# This allows the function to be called externally with different types of numeric inputs, providing flexibility in usage.