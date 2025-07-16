# A Python program to find the longest substring of a given string without duplicate characters.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3003_Longest_Substring_Without_Repeating_Characters.py
# Description: A Python program to find the length of the longest substring without repeating characters.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import time

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    This function uses a sliding window approach to achieve O(n) time complexity.
    """
    if not s:
        return 0

    char_index_map = {}
    max_count = 0
    start = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = index
        max_count = max(max_count, index - start + 1)

    return max_count

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Longest Substring Finder Program!")
    print("\nThis program will find the length of the longest substring without repeating characters.")
    print("You will be prompted to enter a string.")
    print("\nLet's get started!\n")

def prompt_user_for_string() -> str:
    """Prompts the user for a string and returns it."""
    count = 0
    while count < 3:
        count += 1
        user_input = input("Enter a string to find the longest substring without repeating characters: ")
        if isinstance(user_input, str):
            return user_input
        else:
            print("Invalid input. Please enter a valid string.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_longest_substring_length(length: int) -> None:
    """Prints the length of the longest substring without repeating characters."""
    print(f"\nThe length of the longest substring without repeating characters is: {length}")

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program in milliseconds."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_solution_title() -> None:
    """Prints the title of the solution."""
    print("\nSolution: Longest Substring Without Repeating Characters using Sliding Window Approach")

def print_intuition() -> None:
    """Prints the intuition behind the algorithm."""
    print("\nIntuition:")
    print("The algorithm uses a sliding window approach to keep track of the characters in the current substring.")
    print("It maintains a dictionary to store the last index of each character.")
    print("When a repeating character is found, the start of the substring is moved to the right of the last occurrence of that character.")

def print_approach() -> None:
    """Prints the approach used in the algorithm."""
    print("\nApproach:")
    print("1. Initialize a dictionary to store the last index of each character.")
    print("2. Use two pointers: one for the start of the substring and one for the current character.")
    print("3. Iterate through the string, updating the start pointer when a repeating character is found.")
    print("4. Calculate the length of the current substring and update the maximum length found.")

def print_complexity() -> None:
    """Prints the time and space complexity of the algorithm."""
    print("\nTime Complexity: O(n)")
    print("Space Complexity: O(m), where m is the size of the character set, since the dictionary stores at most one entry per unique character.")

def print_code() -> None:
    """Prints the code of the algorithm."""
    print("\nCode:")
    print("    def length_of_longest_substring(s: str) -> int:")
    print("        if not s:")
    print("            return 0")
    print("        char_index_map = {}")
    print("        max_count = 0")
    print("        start = 0")
    print("        for index, char in enumerate(s):")
    print("            if char in char_index_map and char_index_map[char] >= start:")
    print("                start = char_index_map[char] + 1")
    print("            char_index_map[char] = index")
    print("            max_count = max(max_count, index - start + 1)")
    print("        return max_count")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Longest Substring Finder Program!")
    print("\nGoodbye!\n")

def main() -> None:
    """Main function to execute the longest substring finder program."""
    print_welcome_message()
    try:
        user_input = prompt_user_for_string()
        start_time = time.perf_counter()
        length = length_of_longest_substring(user_input)
        end_time = time.perf_counter()
        print_longest_substring_length(length)
        print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
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