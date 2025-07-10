#Python program to print prime numbers in a given range

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0402_Print_Primes_in_Range.py
# Description: A Python program to find and print all prime numbers in a user-specified range
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start: int, end: int) -> list[int]:
    """Print all prime numbers in a given range."""
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers.")
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Prime Number Finder Program!")
    print("\nThis program will find and print all prime numbers in a specified range.")
    print("You will be prompted to enter the start and end of the range.")
    print("The range must be between 2 and 9999, inclusive.")
    print("\nLet's get started!\n")

def prompt_for_range() -> tuple[int, int]:
    """Prompt user for a range and print prime numbers in that range."""
    count = 0
    while count < 3:
        count += 1
        try:
            start = int(input("Enter the start of the range (greater than 1): "))
            end = int(input("Enter the end of the range (maximum 9999): "))
            if start > end:
                print("Start of the range must be less than or equal to the end.")
                count += 1
                continue
            elif start < 2 or end > 9999:
                print("Please ensure the start of the range is greater than 1 and the end of the range less than 10,000.")
                count += 1
                continue
            else:
                return start, end
        except ValueError as e:
            print(f"Invalid input: {e}")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_primes_in_range(primes: list[int], start: int, end: int) -> None:
    """Print prime numbers in the specified range."""
    if primes:
        print(f"\nPrime numbers between {start} and {end}: {primes}")
    else:
        print(f"\nThere are no prime numbers between {start} and {end}.")

def main() -> None:
    print_welcome_message()
    try:
        start, end = prompt_for_range()
        primes = find_primes_in_range(start, end)
        print_primes_in_range(primes, start, end)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Prime Number Finder Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This script finds and prints all prime numbers in a user-specified range.
# It includes error handling for invalid inputs and limits the range to 1-9999.
