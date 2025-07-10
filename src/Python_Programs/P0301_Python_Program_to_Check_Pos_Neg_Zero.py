#A Python program to check if a number is positive, negative, or zero

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0301_Python_Program_to_Check_Pos_Neg_Zero.py
# Description: A Python program to check if a number is positive, negative, or zero.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def check_number(number: float|int) -> str:
    """Check if the number is positive, negative, or zero."""
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number (int or float).")
    numtype = "None"
    if number > 0:
        numtype = "Positive"
    elif number < 0:
        numtype = "Negative"
    else:
        numtype = "Zero"
    return numtype

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Number Checker Program!")
    print("\nThis program will check if a number is positive, negative, or zero.")
    print("You will be prompted to enter a number.")
    print("\nLet's get started!\n")

def prompt_for_input() -> float | None:
    """Prompt the user for a number and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            number = float(input("Please enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if count == 3:
        raise ValueError("Too many invalid attempts. Exiting the program.")


def print_result(numtype: str) -> None:
    """Print the result based on the number type."""
    print(f"\nThe number is: {numtype}")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        number = prompt_for_input()
        numtype = check_number(number)
        print_result(numtype)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Number Checker Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program checks if a number is positive, negative, or zero.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid number.
# The program then checks the number and prints whether it is positive, negative, or zero.
# The program is designed to be user-friendly and robust against invalid inputs.
# The program will input and print the result as float, while the function check_number 
# will take one parameter which can be either float or int.
# The function will return the type of the number as a string: "Positive", "Negative",
# or "Zero".
