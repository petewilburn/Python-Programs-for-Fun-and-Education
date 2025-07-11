# Python program to generate a random number within a specified range

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P1401_Random_Int.py
# Description: A Python program to generate a random integer between 1 and 100.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import random

def generate_random_numbers(num_rands: int, lower_bound: int, upper_bound: int, seed: int | None) -> list[int]:
    """Generate a list of random integers between the specified lower and upper bounds."""
    if not (isinstance(num_rands, int) and num_rands > 0):
        raise ValueError("num_rands must be a positive integer.")
    if not (isinstance(lower_bound, int) and isinstance(upper_bound, int)):
        raise ValueError("Both lower and upper bounds must be integers.")
    if not (lower_bound < upper_bound):
        raise ValueError("Lower bound must be less than upper bound.")
    if seed is not None and not isinstance(seed, int):
        raise ValueError("Seed must be an integer or None.")
    
    random.seed(seed)  # Initialize the random number generator with the seed
    numbers = [random.randint(lower_bound, upper_bound) for _ in range(num_rands)]  # Generate a list of random numbers between the specified bounds

    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All generated numbers must be integers.")
    if len(numbers) == 0:
        raise ValueError("No numbers were generated.")
    if len(numbers) != num_rands:
        raise ValueError(f"Expected {num_rands} random numbers, but got {len(numbers)}.")
    if any(num < lower_bound or num > upper_bound for num in numbers):
        raise ValueError(f"All generated numbers must be between {lower_bound} and {upper_bound}.")
    
    return numbers

def print_welcome_message() -> None:
    """Print a welcome message to the user."""
    print("\nWelcome to the Random Number Generator Program!")
    print("\nThis program will generate a random integer between 1 and 100 by default.")
    print("You also have the option to generate multiple random numbers, specify a range, or use a seed for reproducibility.")
    print("\nLet's get started!\n")

def prompt_user_for_instructions() -> tuple[bool, bool, bool]:
    """Prompt the user for instructions and return them."""
    instructions = [False, False, False]
    count = 0
    while count < 3:
        count += 1
        try:
            choice = input("Would you like to generate multiple random number? (yes/no): ").strip().lower()
            if choice == "yes" or choice == "y":
                instructions[0] = True
            elif choice == "no" or choice == "n":
                instructions[0] = False
            else:
                raise ValueError("Please answer with 'yes' or 'no'.")
            choice = input("Would you like to generate a random number within a specific range? (yes/no): ").strip().lower()
            if choice == "yes" or choice == "y":
                instructions[1] = True
            elif choice == "no" or choice == "n":
                instructions[1] = False
            else:
                raise ValueError("Please answer with 'yes' or 'no'.")
            choice = input("Would you like to generate a random number with a specific seed? (yes/no): ").strip().lower()
            if choice == "yes" or choice == "y":
                instructions[2] = True
            elif choice == "no" or choice == "n":
                instructions[2] = False
            else:
                raise ValueError("Please answer with 'yes' or 'no'.")
            return instructions
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count} attempts left.") 
    raise ValueError("Too many invalid attempts. Exiting the program.")

def prompt_user_for_number_of_randoms() -> int:
    """Prompt the user for the number of random numbers to generate."""
    count = 0
    while count < 3:
        count += 1
        try:
            num_randoms = int(input("Enter the number of random numbers to generate (1-100): "))
            if 1 <= num_randoms <= 100:
                return num_randoms
            else:
                raise ValueError("Please enter a number between 1 and 100.")
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count} attempts left.\n")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def prompt_user_for_range() -> tuple[int, int]:
    """Prompt the user for a range and return it."""
    count = 0
    while count < 3:
        count += 1
        try:
            lower_bound = int(input("Enter the lower bound (1-inf): "))
            upper_bound = int(input("Enter the upper bound (1-inf): "))
            if 1 <= lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                raise ValueError("Please ensure the lower bound is at least 1 and less than the upper bound.")
        except ValueError as e:
            print(f"Invalid input: {e}")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def prompt_user_for_seed() -> int:
    """Prompt the user for a seed value for random number generation."""
    count = 0
    while count < 3:
        count += 1
        try:
            seed = int(input("Enter a seed value (integer): "))
            return seed
        except ValueError as e:
            print(f"Invalid input: {e}. You have {3 - count} attempts left.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_random_number(random_numbers: list[int], lower_bound: int, upper_bound: int, seed: int) -> None:
    """Print the generated random number along with its bounds and seed if provided."""
    if not all(isinstance(random_number, int) for random_number in random_numbers) or not isinstance(lower_bound, int) or not isinstance(upper_bound, int) or (seed is not None and not isinstance(seed, int)):
        raise ValueError("Lower bound, upper bound, and random numbers must be integers.")
    if len(random_numbers) == 0:
        raise ValueError("No random numbers generated.")
    elif len(random_numbers) == 1:
        if seed is not None:
            print(f"\nRandom number generated between {lower_bound} and {upper_bound}: {random_numbers[0]} (Seed: {seed})")
        else:
            print(f"\nRandom number generated between {lower_bound} and {upper_bound}: {random_numbers[0]}")
    else:
        if seed is not None:
            print(f"\nRandom numbers generated between {lower_bound} and {upper_bound} with seed {seed}:")
            for random_number in random_numbers:
                print(random_number)
        else:
            print(f"\nRandom numbers generated between {lower_bound} and {upper_bound}:")
            for random_number in random_numbers:
                print(random_number)

def main():
    print_welcome_message()
    try:
        instructions = prompt_user_for_instructions()
        if instructions[0]:
            num_randoms = prompt_user_for_number_of_randoms()
        if instructions[1]:
            lower_bound, upper_bound = prompt_user_for_range()
        if instructions[2]:
            seed = prompt_user_for_seed()
        random_numbers = generate_random_numbers(num_randoms if instructions[0] else 1, lower_bound if instructions[1] else 1, upper_bound if instructions[1] else 100, seed if instructions[2] else None)
        print_random_number(random_numbers, lower_bound if instructions[1] else 1, upper_bound if instructions[1] else 100, seed if instructions[2] else None)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Random Number Generator Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This code generates a random integer between 1 and 100 and prints it.
# It uses the random module to ensure that the number is different each time the program is run