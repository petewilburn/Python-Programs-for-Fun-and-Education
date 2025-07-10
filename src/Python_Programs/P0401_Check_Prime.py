#A Python program to check if a number is prime - Brute Force Method

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0401_Check_Prime.py
# Description: A Python program to check if a number is prime using the brute force method.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def is_prime(number: int) -> bool:
    """Check if the number is prime."""
    if not isinstance(number, int):               # Ensure the input is an integer
        raise ValueError("Input must be an integer.")
    if number <= 1:                                 # All prime numbers are greater than 1
        return False
    for i in range(2, int(number**0.5) + 1):        # Check divisibility from 2 to the square root of the number
        if number % i == 0:                         # A number cannot be divisible by a number greater than its square root
            return False                            # If the number is divisible by any number other than 1 and itself, it is not prime
    return True                                     # If no divisors were found, the number is prime

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Prime Number Checker Program!")
    print("\nThis program will check if a number is prime using the brute force method.")
    print("You will be prompted to enter a positive integer.")
    print("\nLet's get started!\n")

def prompt_for_input() -> int | None:
    """Prompt the user for a number and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            number = int(input("Please enter a positive integer: "))
            if number < 0:
                print("The number must be positive.")
            elif number == 0:
                print("The number cannot be zero.")
            elif number == 1:
                print("1 is not a prime number.")
            else:
                return number
        except ValueError as e:
            print(f"Invalid input: {e}")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_result(number: int, is_prime: bool) -> None:
    """Print the result based on whether the number is prime."""
    if is_prime:
        print(f"\nThe number {number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        number = prompt_for_input()
        is_prime_result = is_prime(number)
        print_result(number, is_prime_result)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Prime Number Checker Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()