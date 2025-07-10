#Python Program to find the factorial of a number using recursion

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0411_Print_Factorial_Recursion.py
# Description: A Python program to find the factorial of a number using recursion.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------


def calc_factorial(n: int) -> int:
    """Calculates the factorial of a number using recursion."""
    if not isinstance(n, int) or n < 0 or n > 999:
        raise ValueError("Input must be an integer between 0 and 999.")
    try:
        if n == 0:
            return 1
        else:
            return n * calc_factorial(n-1)
    except Exception as e:
        raise RuntimeError("An unexpected error occurred.") from e

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Factorial Calculator Program!")
    print("\nThis program will calculate the factorial of a number using recursion.")
    print("You will be prompted to enter an integer between 0 and 999.")
    print("\nLet's get started!\n")

def prompt_user() -> int | None:
    count = 0
    while count < 3:
        count += 1
        try:
            value = int(input("Enter an integer to find its factorial (0-999): "))
            if 0 <= value <= 999:
                return value
        except ValueError as e:
            print(e)
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_factorial(num: int, factorial_result: int) -> None:
    print(f"The factorial of {num} is: {factorial_result}")

def main() -> None:
    print_welcome_message()
    try:
        num = prompt_user()
        factorial_result = calc_factorial(num)
        print_factorial(num, factorial_result)
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    finally:
        print("\nThank you for using the Factorial Calculator Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code defines a function to calculate the factorial of a number
# using recursion. The main function prompts the user for input and displays the result.