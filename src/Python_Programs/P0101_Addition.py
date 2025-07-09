# A Python Program to perform addition of two numbers provided by the user.

# -----------------------------------------------------------------------------
# File: P0101_Addition.py
# Description: Adds two numbers provided by the user and prints the result.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -----------------------------------------------------------------------------

from typing import Union

def add_numbers(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """
    Returns the sum of two numbers.

    Raises:
        ValueError: If either input is not a number (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a + b

def print_welcome_message() -> None:
    print("Welcome to the Addition Program!")
    print("This program will add two numbers that you provide.")

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
    """Prints the result of the addition."""
    print(f"The sum of {num1} and {num2} is: {result}")

def main() -> None:
    """Main function to execute the addition program."""
    print_welcome_message()
    try:
        num1, num2 = prompt_user_for_numbers()
        result = add_numbers(num1, num2)
        print_result(num1, num2, result)
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for using the Addition Program!")
    print("Goodbye!")

if __name__ == "__main__":
    main()

# This code is a simple addition program that prompts the user for two numbers,
# adds them together, and prints the result. It includes error handling.
# The program will exit after three invalid attempts to enter numbers.
# It also includes a welcome message and functions to handle the main logic, user input, and result printing.
# The program will input and print the result as float, while the function add_numbers will take two parameters, 
# a and b, which can be either float or int.
# The function will return the result of adding a and b, which can also be either float or int.
# This allows the function to be called externally with different types of numeric inputs, providing flexibility in usage.