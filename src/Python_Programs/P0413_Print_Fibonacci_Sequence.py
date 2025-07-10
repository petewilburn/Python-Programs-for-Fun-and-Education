# A Python Program to print the Fibonacci series up to a given number.

# Minimum Python Version: 3.9

# -----------------------------------------------------------------------------
# File: P0413_Print_Fibonacci_Sequence.py
# Description: Prints the Fibonacci sequence up to a user-specified number of terms.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -----------------------------------------------------------------------------

def fibonacci(n: int) -> list:
    """
    Returns a list containing the Fibonacci sequence up to n terms.
    Raises ValueError if n is not a positive integer or exceeds 100.
    """
    if not isinstance(n, int):
        raise ValueError("The number of terms must be an integer.")
    if n <= 0:
        raise ValueError("The number of terms must be a positive integer.")
    if n > 100:
        raise ValueError("The number of terms must not exceed 100.")
    if n == 1:
        return [0]
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Fibonacci Sequence Program!")
    print("This program will generate the Fibonacci sequence up to a specified number of terms.")
    print("You will be prompted to enter the number of terms you want in the sequence.")
    print("\nLet's get started!\n")

def prompt_user_for_number_of_terms() -> int:
    """Prompts the user for the number of terms in the Fibonacci sequence."""
    count = 0
    while count < 3:
        try:
            terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
            if terms <= 0:
                count += 1
                raise ValueError("The number of terms must be a positive integer.")
            if terms > 100:
                count += 1
                raise ValueError("The number of terms must not exceed 100.")
            return terms
        except ValueError as e:
            count += 1
            print(f"Invalid input: {e}. You have {3 - count} attempts left.")
    raise ValueError("Too many invalid attempts. Exiting.")


def print_fibonacci_sequence(sequence: list) -> None:
    """Prints the Fibonacci sequence."""
    print("\nThe Fibonacci sequence is:")
    print(", ".join(map(str, sequence)))

def main():
    """Main function to execute the Fibonacci program."""
    print_welcome_message()
    try:
        num_terms = prompt_user_for_number_of_terms()
        fib_sequence = fibonacci(num_terms)
        print_fibonacci_sequence(fib_sequence)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Fibonacci Sequence Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code is a simple Fibonacci sequence program that prompts the user for the number of terms,
# generates the Fibonacci sequence up to that number, and prints the result. It includes error handling.
# The program will exit after three invalid attempts to enter the number of terms.
# It also includes a welcome message and functions to handle the main logic, user input, and result printing.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# The program ensures that the number of terms is a positive integer and does not exceed 100 terms.
# The Fibonacci sequence is a well-known mathematical sequence that has applications in various fields, including computer science, mathematics, and nature.
# The sequence is defined as follows:
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1