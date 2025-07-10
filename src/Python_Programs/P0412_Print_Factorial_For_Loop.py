#Python Program to find the factorial of a number using a for loop

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0412_Print_Factorial_For_Loop.py
# Description: A Python program to find the factorial of a number using a for loop.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def calc_factorial(num: int) -> int:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num != int(num):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def print_welcome_message():
    print("\nWelcome to the Factorial Calculator Program!")
    print("\nThis program will calculate the factorial of a number using a for loop.")
    print("You will be prompted to enter an integer between 0 and 42.")
    print("\nLet's get started!\n")

def prompt_user() -> int | None:
    count = 0
    while count < 3:
        try:
            value = int(input("Enter an integer to find its factorial (0-42): "))
            if 0 <= value <= 42:
                return value
            else:
                count += 1
                print("Please enter a number between 0 and 42.")
        except ValueError:
            count += 1
            print("Invalid input. Please enter a valid integer. You have {} attempts left.".format(3 - count))
    if count == 3:
        return None

def print_factorial(num: int, factorial_result: int) -> None:
    print(f"The factorial of {num} is: {factorial_result}")

def main() -> None:
    print_welcome_message()
    try:
        num = prompt_user()
        factorial_result = calc_factorial(num)
        print_factorial(num, factorial_result)
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    finally:
        print("\nThank you for using the Factorial Calculator Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code defines a function to calculate the factorial of a number
# using recursion. The main function prompts the user for input and displays the result.