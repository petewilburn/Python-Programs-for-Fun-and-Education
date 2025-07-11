# A Python program to find all Happy Numbers in a given range.

# Minimum Python version 3.9

# -----------------------------------------------------------------------------
# File: P0421_Happy_Numbers_in_Range.py
# Description: A Python program to find all Happy Numbers in a given range.
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

def happy_numbers(lower_bound: int, upper_bound: int) -> list[int]: 
    """Find all happy numbers in a given range."""
    if not (isinstance(lower_bound, int) and isinstance(upper_bound, int)):
        raise ValueError("Both lower_bound and upper_bound must be integers.")
    if lower_bound < 1 or upper_bound > 9999:
        raise ValueError("Range must be between 1 and 9999.")
    
    happy_nums = []
    for num in range(lower_bound, upper_bound + 1):
        if is_happy_number(num):
            happy_nums.append(num)

    if not all(isinstance(num, int) for num in happy_nums):
        raise ValueError("All happy numbers must be integers.")

    return happy_nums

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Happy Numbers Finder!")
    print("\nA Happy Number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.")
    print("For example, 19 is a happy number because:")
    print("1. 1^2 + 9^2 = 82")
    print("2. 8^2 + 2^2 = 68")
    print("3. 6^2 + 8^2 = 100")
    print("4. 1^2 + 0^2 + 0^2 = 1")
    print("\nThis program will find all happy numbers in a specified range.")
    print("You will be prompted to enter the lower and upper bounds of the range.")
    print("The range must be between 1 and 9999, inclusive.")
    print("\nLet's get started!\n")

def prompt_for_range() -> tuple[int, int]:
    """Prompt the user for a range of numbers."""
    count = 0
    while count < 3:
        count += 1
        try:
            lower_bound = int(input("Enter the lower bound of the range (greater than 0): "))
            upper_bound = int(input("Enter the upper bound of the range (maximum 9999): "))
            if lower_bound > upper_bound:
                print("Lower bound must be less than or equal to upper bound.")
                continue
            elif lower_bound < 1 or upper_bound > 9999:
                print("Please ensure the lower bound is greater than 0 and the upper bound is less than or equal to 9999.")
                continue
            return lower_bound, upper_bound
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid integers.\n")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_happy_numbers(lower_bound: int, upper_bound: int) -> None:
    """Print all happy numbers in the specified range."""
    happy_nums = happy_numbers(lower_bound, upper_bound)
    if happy_nums:
        print(f"\nHappy numbers between {lower_bound} and {upper_bound}:")
        for i in range(0, len(happy_nums), 20):
            print(", ".join(map(str, happy_nums[i:i+20])))
    else:
        print(f"\nNo happy numbers found between {lower_bound} and {upper_bound}.") 

def main():
    """Main function to run the Happy Numbers Finder program."""
    print_welcome_message()
    try:
        lower_bound, upper_bound = prompt_for_range()
        print_happy_numbers(lower_bound, upper_bound)
    except ValueError as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Happy Numbers Finder!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program finds all happy numbers in a specified range.
# It prompts the user for the lower and upper bounds of the range,
# validates the input, and then displays all happy numbers within that range.