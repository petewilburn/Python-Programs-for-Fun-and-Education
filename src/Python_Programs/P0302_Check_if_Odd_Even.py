#A Python program to check if an integer is odd or even

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0302_Check_if_Odd_Even.py
# Description: A Python program to check if an integer is odd or even. 
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def check_odd_even(number: int) -> str:
    """Check if the number is odd or even."""
    # Check if the number is even or odd using modulus operator
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    numtype = "None"
    if number == 0:
        numtype = "Zero. Zero is neither odd nor even."
    elif number % 2 == 0:
        numtype = "Even"
    elif number % 2 != 0:
        numtype = "Odd" 
    return numtype

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Odd/Even Checker Program!\n")
    print("\nThis program will check if an integer is odd or even.")
    print("You will be prompted to enter an integer.")
    print("\nLet's get started!\n")

def prompt_for_input() -> int | None:
    """Prompt the user for an integer and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            number = int(input("Please enter an integer: "))
            return number
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(number: int, numtype: str) -> None:
    """Print the result based on the number type."""
    print(f"\nThe number {number} is: {numtype}")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        number = prompt_for_input()
        numtype = check_odd_even(number)
        print_result(number, numtype)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Odd/Even Checker Program!") 
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program checks if an integer is odd or even.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid integer.
# The program then checks the integer and prints whether it is odd or even.
# The program is designed to be user-friendly and robust against invalid inputs.
# It uses a simple modulus operation to determine the odd/even status.
