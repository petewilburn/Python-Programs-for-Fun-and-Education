# A Python Program to perform Division

# ----------------------------------------------------------------------------------------------
# File: P0104_Division.py
# Description: Divides the first number by the second number provided by the user.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ----------------------------------------------------------------------------------------------
from typing import Union

def divide_a_by_b(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    Returns the result of dividing a by b.
    Raises ValueError if inputs are not numbers, 
    and ZeroDivisionError if b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def print_welcome_message() -> None:
    print("Welcome to the Division Program!")
    print("This program will divide the first number by the second number.")

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
    raise ValueError("Too many invalid attempts. Exiting. \n\n   *** Goodbye! ***")

def print_result(num1: float, num2: float, result: float) -> None:
    """Prints the result of the division."""
    print(f"The result of dividing {num1} by {num2} is: {result}")

def main() -> None:
    """Main function to execute the division program."""

    print_welcome_message()
    try:
        num1, num2 = prompt_user_for_numbers()
        result = divide_a_by_b(num1, num2)
        print_result(num1, num2, result)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Thank you for using the Division Program!")
    print("Goodbye!")

if __name__ == "__main__":
    main()

# This code is a simple division program that prompts the user for two numbers,
# divides the first number by the second, and prints the result. It includes error handling.
# The program will exit after three invalid attempts to enter numbers.
# It also includes a welcome message and functions to handle the main logic, user input, and result printing.
# The program will input and print the result as float, while the function divide_a_by_b will take two parameters, 
# a and b, which can be either float or int.
# The function will return the result of dividing a by b, which can also be either float or int.
# This allows the function to be called externally with different types of numeric inputs, providing flexibility in usage.
# The program handles both ValueError for invalid inputs and ZeroDivisionError for division by zero.

