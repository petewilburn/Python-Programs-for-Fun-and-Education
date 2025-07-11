# A Python program to check for a leap year

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P2002_Leap_Year.py
# Description: A Python program to check if a given year is a leap year.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def check_leap_year(year: int) -> bool:
    """Check if the year is a leap year."""
    # A year is a leap year if it is divisible by 4,
    # except for end-of-century years, which must be divisible by 400.
    if not isinstance(year, int):
        raise ValueError("Input must be an integer.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def print_welcome_message() -> None:
    print("\nWelcome to the Leap Year Checker!")
    print("\nThis program will determine if a given year is a leap year.")
    print("You will be prompted to enter a year.")
    print("\nLet's get started!\n")

def prompt_for_input() -> int | None:
    """Prompt the user for a year and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            year = int(input("Please enter a year (e.g., 2023): "))
            if year < 0:
                print("Year must be a positive integer.")
                continue
            return year
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid year.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(year: int, is_leap: bool) -> None:
    """Print the result based on whether the year is a leap year."""
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if not isinstance(is_leap, bool):
        raise ValueError("is_leap must be a boolean value.")
    if is_leap:
        print(f"\n{year} is a leap year.")
    else:
        print(f"\n{year} is not a leap year.")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        year = prompt_for_input()
        is_leap = check_leap_year(year)
        print_result(year, is_leap)
    except ValueError as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Leap Year Checker!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program checks if a year is a leap year.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid year.
# The program then checks the year and prints whether it is a leap year or not.
# The program is designed to be user-friendly and robust against invalid inputs.
# It uses the rules of leap years to determine the result.