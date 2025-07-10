#Python program to print a multiplication table for a given number

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0501_Print_the_Multiplication_Table_of_a_Number.py
# Description: A Python program to print the multiplication table for a given number.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def print_multiplication_table(number: int) -> None:
    """Print the multiplication table for the given number."""
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i} \n")

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Multiplication Table Program!")
    print("\nThis program will print the multiplication table for a given number.")
    print("You will be prompted to enter a positive integer.")
    print("\nLet's get started!\n")

def prompt_for_number() -> int | None:
    """Prompt the user for a number and return it."""
    count = 0
    while count < 3:
        try:
            number = int(input("Please enter a positive integer: "))
            if number <= 0:
                raise ValueError("The number must be positive.")
            return number
        except ValueError as e:
            print(f"Invalid input: {e}")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_multiplication_table_of_number(number: int) -> None:
    """Print the multiplication table of the given number."""
    print(f"\nMultiplication Table for {number}:")
    print_multiplication_table(number)

def main():
    print_welcome_message()
    try:
        number = prompt_for_number()
        if number is not None:
            print_multiplication_table_of_number(number)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Multiplication Table Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program prints the multiplication table for a given positive integer.
# It includes error handling for invalid inputs and provides a user-friendly interface.
# The user is prompted to enter a positive integer, and the multiplication table is printed from 1 to 10.
# The program will exit after three invalid attempts to enter a number.