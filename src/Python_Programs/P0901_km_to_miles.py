#Python program to convert kilometers to miles

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0901_km_to_miles.py
# Description: A Python program to convert kilometers to miles.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def km_to_miles(km: float) -> float:
    if not isinstance(km, (int, float)):
        raise ValueError("Input must be a number (int or float).")
    # 1 kilometer is approximately equal to 0.621371 miles
    return km * 0.621371

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Kilometers to Miles Converter Program!")
    print("\nThis program will convert kilometers to miles.")
    print("You will be prompted to enter a distance in kilometers.")
    print("\nLet's get started!\n")

def print_conversion(km: float) -> None:
    miles = km_to_miles(km)
    print(f"\n{km} kilometers is equal to {miles:.2f} miles.")

def prompt_for_km() -> float:
    """Prompt the user for a distance in kilometers and return it."""
    count = 0
    while count < 3:
        try:
            km = float(input("Please enter a distance in kilometers: "))
            if km < 0:
                raise ValueError("Distance cannot be negative.")
            return km
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count - 1} attempts left.")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting the program.")

def main() -> None:
    print_welcome_message()
    try:
        km = prompt_for_km()
        print_conversion(km)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Kilometers to Miles Converter Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program converts kilometers to miles.
# It prompts the user to enter a distance in kilometers and then calculates the equivalent distance in miles
# Example usage:
# Enter distance in kilometers: 5
# 5 kilometers is equal to 3.11 miles.