# A Python program to find the number of palindromic substrings in a given string

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3647_Palindromic_Substrings.py
# Description: A Python program to count the number of palindromic substrings in a given string.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import time

def count_substrings(s: str) -> int:
    """
    Counts the number of palindromic substrings in a given string s.
    This function uses a center expansion approach to achieve O(n^2) time complexity.
    """
    if not s:                                                             # If the string is empty, return 0
        return 0

    count = 0

    def expand_around_center(left: int, right: int) -> None:              # Helper function expands around the center and counts palindromic substrings
        nonlocal count                                                    # This allows the inner function to modify the count variable in the outer scope
        while left >= 0 and right < len(s) and s[left] == s[right]:       # Expand while the characters are equal
            count += 1                                                    # Increment the count for each palindromic substring found
            left -= 1                                                     # Move left pointer to the left
            right += 1                                                    # Move right pointer to the right

    for i in range(len(s)):                                               # For each character in the string
        expand_around_center(i, i)                                        # Check for Odd length palindromes
        expand_around_center(i, i + 1)                                    # Check for Even length palindromes

    return count                                                          # Return the total count of palindromic substrings

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Palindromic Substrings Counter Program!")
    print("\nThis program will count the number of palindromic substrings in a given string.")
    print("You will be prompted to enter a string.")
    print("\nLet's get started!\n")

def prompt_user_for_string() -> str:
    """Prompts the user to enter a string and returns it."""
    count = 0
    while count < 3:                                                      # Allow up to 3 attempts for valid input
        count += 1
        user_input = input("Enter a string to count palindromic substrings: ")
        if isinstance(user_input, str):
            return user_input
        else:
            print("Invalid input. Please enter a valid string.")
    raise ValueError("Too many invalid attempts. Exiting the program.")   # Raise an error if too many invalid attempts

def print_palindromic_substring_count(count: int) -> None:
    """Prints the count of palindromic substrings."""
    print(f"\nThe number of palindromic substrings is: {count}")

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program in milliseconds."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_solution_title() -> None:
    """Prints the title of the solution."""
    print("\nSolution Title: Count of Palindromic Substrings using a Center Expansion Approach")
    
def print_intuition() -> None:
    """Prints the intuition behind the algorithm."""
    print("\nIntuition:")
    print("The algorithm expands around each character to find odd-length palindromes.")
    print("The algorithm also expands outwards from sequential pairs to find even-length palindromes.")
    print("For single characters, it checks for both odd length palindromes by expanding outwards until the characters no longer match.")
    print("For sequential pairs of characters, it checks for even length palindromes in a similar manner.")

def print_approach() -> None:
    """Prints the approach used in the solution."""
    print("\nApproach:")
    print("Odd length palindromes: (expand_around_center(i, i))")
    print("1. For each character in the string, treat it as a center and expand outwards to find palindromic substrings.")
    print("2. Count each valid palindrome found during the expansion.")
    print("3. Return the total count of palindromic substrings.")
    print("Even length palindromes: (expand_around_center(i, i + 1))")
    print("1. For each pair of sequential characters in the string, treat the space between them as a center and expand outwards to find palindromic substrings.")
    print("2. Count each valid palindrome found during the expansion.")
    print("3. Return the total count of palindromic substrings.")

def print_complexity() -> None:
    """Prints the time and space complexity of the solution."""
    print("\nTime Complexity: O(n²)")
    print("\nTime Complexity Derivation:")
    print("1. Outer loop: We iterate through each character in the string → O(n)")
    print("2. For each character, we call expand_around_center twice:")
    print("   - Once for odd-length palindromes: expand_around_center(i, i)")
    print("   - Once for even-length palindromes: expand_around_center(i, i + 1)")
    print("3. Each expand_around_center call can potentially expand up to n/2 times in the worst case")
    print("4. Mathematical analysis:")
    print("   - Best case: Each expansion stops immediately → O(n)")
    print("   - Worst case: String like 'aaaa...' where every expansion goes to full length")
    print("   - For position i, maximum expansion is min(i, n-1-i)")
    print("   - Total operations: Σ(i=0 to n-1) min(i, n-1-i) ≈ n²/4")
    print("   - Therefore: O(n²)")
    print("\nSpace Complexity: O(1) - The algorithm uses a constant amount of space for counting.")
    print("- Only variables: count, left, right pointers")
    print("- No additional data structures that grow with input size")

def print_code() -> None:
    """Prints the code of the solution."""
    print("\nCode:")
    print("def count_substrings(s: str) -> int:")
    print("    if not s:")
    print("        return 0")
    print("    count = 0")
    print("    def expand_around_center(left: int, right: int) -> None:")
    print("        nonlocal count")
    print("        while left >= 0 and right < len(s) and s[left] == s[right]:")
    print("            count += 1")
    print("            left -= 1")
    print("            right += 1")
    print("    for i in range(len(s)):")
    print("        expand_around_center(i, i)")
    print("        expand_around_center(i, i + 1)")
    print("    return count")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Palindromic Substrings Counter Program!")
    print("We hope you found it helpful in counting palindromic substrings in your string.")
    print("\nGoodbye!\n")

def main() -> None:
    """Main function to run the program."""
    print_welcome_message()
    try:
        user_input = prompt_user_for_string()
        start_time = time.perf_counter()  # Start the timer
        count = count_substrings(user_input)  # Count palindromic substrings
        end_time = time.perf_counter()  # End the timer
        print_palindromic_substring_count(count)  # Print the count
        print_runtime((end_time - start_time) * 1000)  # Print the runtime in milliseconds
        print_solution_title()  # Print the solution title
        print_intuition()  # Print the intuition behind the algorithm
        print_approach()  # Print the approach used in the solution
        print_complexity()  # Print the time and space complexity
        print_code()  # Print the code of the solution
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print_thank_you_message()  # Print thank you message

if __name__ == "__main__":
    main()  # Run the main function

# This code implements a solution to count the number of palindromic substrings in a given string using a center expansion approach.
# The program prompts the user for a string, counts the palindromic substrings,
# and prints the count along with the runtime of the algorithm.
# The solution has a time complexity of O(n^2) and a space complexity of O
#(1), making it efficient for moderate-sized strings.

