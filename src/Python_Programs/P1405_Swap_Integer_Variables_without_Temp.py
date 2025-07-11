#Python program to swap two integer variables without using a third variable

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P1405_Swap_Integer_Variables_without_Temp.py
# Description: A Python program to swap two integer variables without using a third variable.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def swap_variables(a: int, b: int) -> tuple[int, int]:
    """Swap two variables without using a third variable.
    Using tuple unpacking to swap values """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    a, b = b, a
    return a, b

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Variable Swap Program!")
    print("This program will swap two integer variables without using a third variable.")
    print("You will be prompted to enter two integers.")
    print("\nLet's get started!\n")

def prompt_for_input() -> tuple[int, int] | None:
    """Prompt the user for two integers and return them."""
    count = 0
    while count < 3:
        try:
            a = int(input("Enter the first integer (a): "))
            b = int(input("Enter the second integer (b): "))
            return a, b
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count} attempts left.")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(a: int, b: int) -> None:
    """
    Print the values before and after swapping.
    :param a: First variable after swap
    :param b: Second variable after swap
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both values must be integers.")
    print(f"\nBefore Swap, Values: a = {b}, b = {a}")
    print(f"After Swap, Values: a = {a}, b = {b}")

def main():
    """Main function to execute the swap operation."""
    print_welcome_message()
    try:
        a, b = prompt_for_input()
        a, b = swap_variables(a, b)
        print_result(a, b)
    except ValueError as e:
        print(e)
        return
    finally:
        print("\nThank you for using the Variable Swap Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This program has a function that swaps two variables without using a third variable.
# It prompts the user for input, performs the swap, and prints the results. 
# The swap is done using tuple unpacking in Python, which is a concise way to swap values.
# The program also handles invalid input gracefully by catching ValueError exceptions.



