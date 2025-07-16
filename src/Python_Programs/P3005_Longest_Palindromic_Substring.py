# A Python program to find the longest palindromic substring in a given string s.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3005_Longest_Palindromic_Substring.py
# Description: A Python program to find the longest palindromic substring in a given string
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import time

def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in a given string s.
    This function uses a center expansion approach to achieve O(n^2) time complexity.
    """
    if not s:
        return ""

    start, end = 0, 0

    def expand_around_center(s: str, left: int, right: int) -> int:
        """Expands around the center and returns the length of the palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # Odd length palindrome
        len2 = expand_around_center(s, i, i + 1)  # Even length palindrome
        max_length = max(len1, len2)

        if max_length > end - start:
            start = i - (max_length - 1) // 2
            end = i + max_length // 2

    return s[start:end + 1]

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Longest Palindromic Substring Finder Program!")
    print("\nThis program will find the longest palindromic substring in a given string.")
    print("You will be prompted to enter a string.")
    print("\nLet's get started!\n")

def prompt_user_for_string() -> str:
    """Prompts the user to enter a string and returns it."""
    count = 0
    while count < 3:
        count += 1
        user_input = input("Enter a string to find the longest palindromic substring: ")
        if isinstance(user_input, str):
            return user_input
        else:
            print("Invalid input. Please enter a valid string.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_longest_palindromic_substring(substring: str) -> None:
    """Prints the longest palindromic substring found."""
    print(f"\nThe longest palindromic substring is: '{substring}'")

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program in milliseconds."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_solution_title() -> None:
    """Prints the title of the solution."""
    print("\nSolution: Longest Palindromic Substring using Center Expansion Approach")

def print_intuition() -> None:
    """Prints the intuition behind the algorithm."""
    print("\nIntuition:")
    print("The algorithm expands around each character (and between characters) to find palindromes.")
    print("It checks both odd and even length palindromes by expanding outwards from the center.")

def print_approach() -> None:
    """Prints the approach used in the solution."""
    print("\nApproach:")
    print("1. Iterate through each character in the string.")
    print("2. For each character, expand around it to find the longest palindrome.")
    print("3. Keep track of the start and end indices of the longest palindrome found.")

def print_complexity() -> None:
    """Prints the time and space complexity of the algorithm."""
    print("\nTime Complexity: O(n^2)")
    print("Space Complexity: O(1) - No extra space used for storing results.")

def print_code() -> None:
    """Prints the code of the solution."""
    print("\nCode:")
    print("    def longest_palindromic_substring(s: str) -> str:")
    print("        if not s:")
    print("            return \"\"")
    print("        start, end = 0, 0")
    print("        def expand_around_center(s: str, left: int, right: int) -> int:")
    print("            while left >= 0 and right < len(s) and s[left] == s[right]:")
    print("                left -= 1")
    print("                right += 1")
    print("            return right - left - 1")
    print("        for i in range(len(s)):")
    print("            len1 = expand_around_center(s, i, i)  # Odd length palindrome")
    print("            len2 = expand_around_center(s, i, i + 1)  # Even length palindrome")
    print("            max_length = max(len1, len2)")
    print("            if max_length > end - start:")
    print("                start = i - (max_length - 1) // 2")
    print("                end = i + max_length // 2")
    print("        return s[start:end + 1]")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Longest Palindromic Substring Finder!")
    print("\nGoodbye!\n")

def main():
    print_welcome_message()
    try:
        user_input = prompt_user_for_string()
        start_time = time.perf_counter()
        longest_palindrome = longest_palindromic_substring(user_input)
        end_time = time.perf_counter()
        print_longest_palindromic_substring(longest_palindrome)
        print_runtime((end_time - start_time) * 1000)
        print_solution_title()
        print_intuition()
        print_approach()
        print_complexity()
        print_code()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print_thank_you_message()

if __name__ == "__main__":
    main()

# This program finds the longest palindromic substring in a given string.
# It uses a center expansion approach to achieve O(n^2) time complexity.
# The user is prompted to enter a string, and the program handles invalid inputs gracefully.
# The program prints the longest palindromic substring found and the runtime in milliseconds.
# The solution includes detailed explanations of the intuition, approach, and complexity.
