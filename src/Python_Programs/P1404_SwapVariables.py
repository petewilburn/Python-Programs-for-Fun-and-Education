# Swap two variables in Python

# Minimum Python version: 3.9

# -----------------------------------------------------------------------------
# File: P1404_SwapVariables.py
# Description: Swaps two variables using a temporary variable.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -----------------------------------------------------------------------------

def swap_variables(a, b):
    """
    Swap two variables using a temporary variable.
    
    :param a: First variable
    :param b: Second variable
    :return: Tuple containing swapped values (b, a)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers (int or float).")
    
    temp = a
    a = b
    b = temp
    #print(f"Swapped values: a = {a}, b = {b}")
    return a, b

def print_welcome_message():
    """
    Print a welcome message to the user.
    """
    print("\nWelcome to the Variable Swap Program!")
    print("This program will swap two variables using a temporary variable.")
    print("You will be prompted to enter two numbers.")
    print("\nLet's get started!\n")

def prompt_user_for_numbers():
    """
    Prompt the user for two numbers to swap.
    """
    count = 0
    while count < 3:
        count += 1
        try:
            a = float(input("Enter the first number (a): "))
            b = float(input("Enter the second number (b): "))
            return a, b
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count} attempts left.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(a, b):
    """
    Print the result of the swap operation.
    
    :param a: First variable after swap
    :param b: Second variable after swap
    """
    print(f"Before Swap, Values: a = {b}, b = {a}")
    print(f"\nAfter Swap, Values: a = {a}, b = {b}\n")

def main():
    """
    Main function to execute the variable swap program.
    """
    print_welcome_message()
    try:
        a, b = prompt_user_for_numbers()
        a, b = swap_variables(a, b)
        print_result(a, b)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nThank you for using the Variable Swap Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code is a simple program that swaps two variables using a temporary variable.
# It prompts the user for two numbers, swaps them, and prints the result.

