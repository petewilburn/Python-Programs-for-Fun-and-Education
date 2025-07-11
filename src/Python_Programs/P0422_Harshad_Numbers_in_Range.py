# A Python program to print all Harshad numbers in a given range.

# Minimum Python version 3.9

# ---------------------------------------------------------------------------------------------
# File: P0422_Check_Harshad_Number.py
# Description: A Python program to find all Harshad numbers in a specified range.
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

def find_harshad_numbers(lower_bound: int, upper_bound: int) -> list[int]:
    """Find all Harshad numbers in a given range."""
    if lower_bound < 1 or upper_bound < 1:
        raise ValueError("Both bounds must be positive integers.")
    if lower_bound > upper_bound:
        raise ValueError("Lower bound must be less than or equal to upper bound.")
    
    harshad_numbers = []
    for number in range(lower_bound, upper_bound + 1):
        if is_harshad_number(number):
            harshad_numbers.append(number)
    
    if not all(isinstance(num, int) for num in harshad_numbers):
        raise ValueError("All found Harshad numbers must be integers.")
    
    return harshad_numbers

def print_welcome_message():
    """Print a welcome message."""
    print("\nWelcome to the Harshad Number Finder!")
    print("This program will find all Harshad numbers in a specified range.")
    print("A Harshad number is an integer that is divisible by the sum of its digits.")
    print("For example, 18 is a Harshad number because the sum of its digits (1 + 8 = 9) divides 18 evenly (18 % 9 == 0).")
    print("88 is not a Harshad number because the sum of its digits (8 + 8 = 16) does not divide 88 evenly (88 % 16 != 0).")
    print("You will be prompted to enter the start and end of the range.\n")

def prompt_for_range():
    """Prompt the user for a range."""
    while True:
        try:
            start = int(input("Please enter the start of the range (positive integer): "))
            end = int(input("Please enter the end of the range (positive integer): "))
            if start < 1 or end < 1:
                raise ValueError("Both start and end must be positive integers.")
            if start > end:
                raise ValueError("Start must be less than or equal to end.")
            return start, end
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")

def print_harshad_numbers(harshad_numbers: list[int], lower_bound: int, upper_bound: int):
    """Print the list of Harshad numbers."""
    if not harshad_numbers:
        print("No Harshad numbers found in the specified range.")
    else:
        print(f"Harshad numbers in the specified range ({lower_bound} to {upper_bound}):")
        for i in range(0, len(harshad_numbers), 20):
            print(", ".join(map(str, harshad_numbers[i:i+20])))

def main():
    """Main function to run the Harshad number finder."""
    print_welcome_message()
    
    try:
        lower_bound, upper_bound = prompt_for_range()
        harshad_numbers = find_harshad_numbers(lower_bound, upper_bound)
        print_harshad_numbers(harshad_numbers, lower_bound, upper_bound)
    except ValueError as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Harshad Number Finder!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program is designed to find all Harshad numbers in a specified range.
# It includes input validation, a welcome message, and handles exceptions gracefully.
# A Harshad number is also known as a Niven number.
# A Harshad number is a number that is divisible by the sum of its digits.