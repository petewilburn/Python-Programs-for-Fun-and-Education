# A Python program to check if a number is a Happy Number.

# Minimum Python version 3.9

# -----------------------------------------------------------------------------
# File: P0420_Check_Happy_Number.py
# Description: A Python program to check if a number is a happy number.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -----------------------------------------------------------------------------

def is_happy_number(number: int) -> bool:
    """Check if a number is a happy number."""
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1

def print_welcome_message() -> None:
    print("\nWelcome to the Happy Number Checker!")
    print("\nThis program will determine if a given number is a Happy Number.")
    print("You will be prompted to enter a number.")
    print("\nLet's get started!\n")

def prompt_for_input() -> int | None:
    """Prompt the user for a number and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            num = int(input("Please enter a number (1-9999): "))
            if num < 1:
                raise ValueError("Number must be a positive integer.")
            if num > 9999:
                raise ValueError("Number must be less than or equal to 9999.")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.\n")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(num: int, is_happy: bool) -> None:
    """Print the result based on whether the number is a happy number."""
    if not isinstance(num, int):
        raise ValueError("Number must be an integer.")
    if not isinstance(is_happy, bool):
        raise ValueError("is_happy must be a boolean value.")
    if is_happy:
        print(f"\n{num} is a happy number.")
    else:
        print(f"\n{num} is not a happy number.")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        num = prompt_for_input()
        is_happy = is_happy_number(num)
        print_result(num, is_happy)
    except ValueError as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Happy Number Checker!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program checks if a number is a happy number.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid number.
# The program then checks the number and prints whether it is a happy number or not.
# The program is designed to be user-friendly and robust against invalid inputs.
# It uses the rules of happy numbers to determine the result.