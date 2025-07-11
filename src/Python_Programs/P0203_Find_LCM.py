# A Python program to find the Least Common Multiple (LCM) of two numbers.

# Minimum Python version 3.9

# ---------------------------------------------------------------------------------------------
# File: P0203_Find_LCM.py
# Description: A Python program to find the Least Common Multiple (LCM) of two numbers.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def find_lcm(a: int, b: int) -> int:
    """Finds the Least Common Multiple (LCM) of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive integers.")

    def gcd(x: int, y: int) -> int:
        """Helper function to compute the Greatest Common Divisor (GCD)."""
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

def print_welcome_message() -> None:
    """Prints a welcome message for the LCM finder program."""
    print("\nWelcome to the LCM Finder!")
    print("\nThis program will help you find the Least Common Multiple (LCM) of two positive integers.")
    print("You will be prompted to enter two positive integers.")
    print("\nLet's get started!\n")

def prompt_user_for_numbers() -> tuple[int, int]:
    """Prompts the user for two positive integers and returns them as a tuple."""
    count = 0
    while count < 3:
        try:
            num1 = int(input("Enter the first positive integer: "))
            num2 = int(input("Enter the second positive integer: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid positive integers.")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting. \n\n   *** Goodbye! ***")

def print_result(num1: int, num2: int, lcm: int) -> None:
    """Prints the result of the LCM calculation."""
    print(f"\nThe Least Common Multiple (LCM) of {num1} and {num2} is: {lcm}")

def main() -> None:
    """Main function to execute the LCM finder program."""
    print_welcome_message()
    try:
        num1, num2 = prompt_user_for_numbers()
        lcm = find_lcm(num1, num2)
        print_result(num1, num2, lcm)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nThank you for using the LCM Finder!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code is a simple program that calculates the Least Common Multiple (LCM) of two positive integers.
# It includes input validation, a welcome message, and handles exceptions gracefully.
