# Python program to generate a random number between 1 and 100

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P1401_Random_Int.py
# Description: A Python program to generate a random integer between 1 and 100.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import random

def generate_random_number():
    random.seed()  # Initialize the random number generator
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    return number

def print_welcome_message():
    """Print a welcome message to the user."""
    print("\nWelcome to the Random Number Generator Program!")
    print("\nThis program will generate a random integer between 1 and 100.")
    print("Each time you run the program, a different number will be generated.")
    print("\nLet's get started!\n")

def print_random_number():
    random_number = generate_random_number()
    print(f"Random number generated: {random_number}")
# Main function to execute the random number generation

def main():
    print_welcome_message()
    print_random_number()
    print("\nThank you for using the Random Number Generator Program!")
    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code generates a random integer between 1 and 100 and prints it.
# It uses the random module to ensure that the number is different each time the program is run