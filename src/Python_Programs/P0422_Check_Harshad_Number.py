# A Python program to check whether a number is a Harshad number

# Minimum Python version 3.9

# ---------------------------------------------------------------------------------------------
# File: P0422_Check_Harshad_Number.py
# Description: A Python program to check if a number is a Harshad number.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def is_harshad_number(number: int) -> bool:
    """Check if a number is a Harshad number."""
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0

def print_welcome_message() -> None:
    print("\nWelcome to the Harshad Number Checker!")
    print("\nThis program will determine if a given number is a Harshad number.")
    print("A Harshad number is an integer that is divisible by the sum of its digits.")
    print("For example:")
    print("     18 is a Harshad number because the sum of its digits (1 + 8 = 9) divides 18 evenly (18 % 9 == 0).")
    print("     88 is not a Harshad number because the sum of its digits (8 + 8 = 16) does not divide 88 evenly (88 % 16 != 0).")
    print("You will be prompted to enter a positive integer.")
    print("\nLet's get started!\n")

def prompt_for_number() -> int:
    """Prompt the user for a positive integer."""
    count = 0
    while count < 3:
        count += 1
        try:
            num = int(input("Please enter a positive integer: "))
            if num <= 0:
                raise ValueError("Number must be a positive integer.")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.\n")
    
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(num: int, is_harshad: bool) -> None:
    """Print the result of the Harshad number check."""
    if is_harshad:
        print(f"\n{num} is a Harshad number.")
    else:
        print(f"\n{num} is not a Harshad number.")

def main() -> None:
    """Main function to run the Harshad number checker."""
    print_welcome_message()
    
    try:
        num = prompt_for_number()
        is_harshad = is_harshad_number(num)
        print_result(num, is_harshad)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Harshad Number Checker!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code checks if a number is a Harshad number, which is an integer that is divisible by the sum of its digits.
# It includes input validation, a welcome message, and handles exceptions gracefully.
# A Harshad number is also known as a Niven number.
# A Harshad number is a number that is divisible by the sum of its digits.
# For example, 18 is a Harshad number because the sum of its digits (1 + 8 = 9) divides 18 evenly (18 % 9 == 0).
# 88 is not a Harshad number because the sum of its digits (8 + 8 = 16) does not divide 88 evenly (88 % 16 != 0).