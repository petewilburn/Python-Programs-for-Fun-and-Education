# A Python program to find the Least Common Denominator (LCD) of two or more fractions.

# Minimum Python version 3.9

# ---------------------------------------------------------------------------------------------
# File: P0202_Find_LCD.py
# Description: A Python program to find the Least Common Denominator (LCD) of two or more numbers.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.   
# ---------------------------------------------------------------------------------------------

def find_lcd(numbers: list[tuple[int, int]]) -> int:
    """Finds the Least Common Denominator (LCD) of a list of fractions."""
    if not isinstance(numbers, list) or not all(isinstance(num, tuple) and len(num) == 2 for num in numbers):
        raise ValueError("Input must be a list of fractions represented as tuples.")
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to find the LCD.")
    
    denominators = [denom for _, denom in numbers]
    if any(denom <= 0 for denom in denominators):
        raise ValueError("Denominators must be positive integers.")

    lcd = denominators[0]
    for denom in denominators[1:]:
        lcd = lcm(lcd, denom)
    return lcd

def gcd(x: int, y: int) -> int:
    """Helper function to compute the Greatest Common Divisor (GCD)."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both inputs must be integers.")
    while y:
        x, y = y, x % y
    return x

def lcm(x: int, y: int) -> int:
    """Helper function to compute the Least Common Multiple (LCM)."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Both inputs must be integers.")
    return abs(x * y) // gcd(x, y)

def print_welcome_message() -> None:
    """Prints a welcome message for the LCD finder program."""
    print("\nWelcome to the LCD Finder!")
    print("\nThis program will help you find the Least Common Denominator (LCD) of two or more fractions.")
    print("You will be prompted to enter a list of fractions.")
    print("\nLet's get started!\n")

def prompt_user_for_numbers() -> list[tuple[int, int]]:
    """Prompts the user for a list of fractions and returns them as a list of tuples (numerator, denominator)."""
    count = 0
    numbers = []
    while count < 3:
        try:
            input_str = input("Enter fractions as 'numerator/denominator' separated by commas (e.g., 1/2, 3/4): ")
            fractions = input_str.split(',')
            for fraction in fractions:
                num, denom = map(int, fraction.strip().split('/'))
                if denom == 0:
                    raise ValueError("Denominator cannot be zero.")
                numbers.append((num, denom))
            if len(numbers) < 2:
                raise ValueError("At least two fractions are required.")
            return numbers
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid fractions.\n")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting. \n\n   *** Goodbye! ***")

def print_result(numbers: list[tuple[int, int]], lcd: int) -> None:
    """Prints the result of the LCD calculation."""
    numbers_str = ', '.join(f"{num}/{denom}" for num, denom in numbers)
    print(f"\nThe Least Common Denominator (LCD) of {numbers_str} is: {lcd}\n")

def main() -> None:
    """Main function to execute the LCD finder program."""
    print_welcome_message()
    try:
        numbers = prompt_user_for_numbers()
        lcd = find_lcd(numbers)
        print_result(numbers, lcd)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nThank you for using the LCD Finder!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program finds the Least Common Denominator (LCD) of two or more fractions.
# It includes input validation, a welcome message, and handles exceptions gracefully.