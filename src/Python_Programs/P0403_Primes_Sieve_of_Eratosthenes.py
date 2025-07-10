# A Python Program to print all prime numbers in an interval
# using the Sieve of Eratosthenes algorithm

# Minimum Python version: 3.9

# -----------------------------------------------------------------------------
# File: P0403_Primes_Sieve_of_Eratosthenes.py
# Description: A Python program to find and print all prime numbers up to 
# a user-specified limit using the Sieve of Eratosthenes algorithm.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -----------------------------------------------------------------------------


def sieve_of_eratosthenes(n: int) -> list[int]:
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm."""
    if not isinstance(n, int) or n < 2 or n >= 100000:
        raise ValueError("Input must be an integer greater than or equal to 2 and less than 100,000.")
    try:
        primes = []
        is_prime = [True] * (n + 1)                             # Create a boolean array "is_prime[0..n]" and initialize all entries as true.
        is_prime[0] = is_prime[1] = False                       # 0 and 1 are not prime numbers

        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:                                     # If is_prime[p] is still true, then it is a prime number
                for multiple in range(p * p, n + 1, p):         # Mark all multiples of p as not prime
                    is_prime[multiple] = False
        primes = [p for p in range(2, n + 1) if is_prime[p]]   # Collect all primes after sieving
        return primes
    except MemoryError:
        raise MemoryError("The input number is too large to handle with the Sieve of Eratosthenes algorithm.")
    except Exception as e:
        raise RuntimeError("An unexpected error occurred.") from e
    
def print_welcome_message():
    """Prints a welcome message to the user."""
    print("\nWelcome to the Prime Number Finder Program!")
    print("\nThis program will find and print all prime numbers up to a specified limit.")
    print("You will be prompted to enter an upper limit (2 to 99,999).")
    print("\nLet's get started!\n")

def prompt_user_for_input() -> int | None:
    """Prompts the user for an upper limit and returns it."""
    count = 0
    while count < 3:
        count += 1
        try:
            number = int(input("Enter an upper limit (2 to 99,999) to find prime numbers: "))
            if 2 <= number < 100000:
                return number
            else:
                print("The number must be between 2 and 99,999.")
        except ValueError:
            print("Please enter a valid integer.")

def print_primes(primes):
    """Prints the list of prime numbers, summarizing if the list is very long."""
    if not primes:
        print("No prime numbers found.")
        return
    max_row = 20
    if len(primes) <= max_row:
        print("Prime numbers:", ', '.join(map(str, primes)))
    else:
        print(f"\nPrime numbers:")
        for i in range(0, len(primes), max_row):
            print(', '.join(map(str, primes[i:i + max_row])))

def main():
    """Main function to execute the Sieve of Eratosthenes and print prime numbers."""
    print_welcome_message()
    try:
        number = prompt_user_for_input()
        primes = sieve_of_eratosthenes(number)
        print_primes(primes)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Prime Number Finder Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()


# This code will prompt the user for an upper limit and print all prime numbers up to that limit using the Sieve of Eratosthenes algorithm.
# The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified integer n.
# It works by iteratively marking the multiples of each prime number starting from 2.   
# The time complexity of this algorithm is O(n log log n), making it very efficient for large values of n.
# The space complexity is O(n) due to the storage of the boolean array. 
# The program handles edge cases by checking if the input is less than 2 and informs the user accordingly.
# The output is a list of prime numbers, which can be used for further processing or analysis.
# The program is designed to be user-friendly, providing clear instructions and output formatting.  

