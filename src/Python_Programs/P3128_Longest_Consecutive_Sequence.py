# A Python program to find the length of the longest consecutive subsequence in an unsorted array of integers

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3128_Longest_Consecutive_Sequence.py
# Description: A Python program to find the length of the longest consecutive subsequence in an uns
# sorted array of integers.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import time

def hash_longest_consecutive_subsequence_length(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive subsequence in an unsorted array of integers.
    This function uses a set to achieve O(n) time complexity.
    :param nums: List of integers
    :return: Length of the longest consecutive subsequence
    """
    if not nums:
        return 0

    num_set = set(nums)  # Convert list to set for O(1) lookups
    max_count = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            count = 1

            while current_num + 1 in num_set:
                current_num += 1
                count += 1

            max_count = max(max_count, count)

    return max_count


def alt_longest_consecutive_subsequence_length(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive subsequence in an unsorted array of integers.
    This function uses different approaches based on the size of the input list.
    :param nums: List of integers
    :return: Length of the longest consecutive subsequence
    """
    max_count = len(nums)
    if max_count <= 1:
        if max_count == 0:
            return 0
        else:
            return 1
    elif max_count <= 100000:
        nums.sort()
        count = 1
        max_count = 0
        number = nums[0]
        for num in nums:
            if num == number + 1:
                count += 1
            elif num == number:
                pass
            else:
                max_count = max(max_count, count)
                count = 1
            number = num
        max_count = max (max_count, count)
        return max_count
    else:
        num_set = set(nums)
        max_count = 0
        for num in nums:
            if num in num_set and (num - 1) not in num_set:
                number = num
                count = 0
                while number in num_set:
                    num_set.remove(number)
                    number += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Longest Consecutive Subsequence Finder!")
    print("\nThis program will find the length of the longest consecutive subsequence in an unsorted array of integers.")
    print("You will be prompted to enter a list of integers.")
    print("\nLet's get started!\n")

def prompt_user_for_approach() -> str:
    """Prompts the user to choose an approach for finding the longest consecutive subsequence."""
    count = 0
    while count < 3:
        count += 1
        try:
            approach = input("Choose an approach (hash or alt): ").strip().lower()
            if approach in ["hash", "alt"]:
                return approach
            else:
                print("Invalid choice. Please enter 'hash' or 'alt'.")
        except Exception as e:
            print(f"An error occurred: {e}. You have {3 - count} attempts left.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def prompt_user_for_input() -> list[int]:
    """Prompts the user for a list of integers and returns it."""
    count = 0
    while count < 3:
        count += 1
        try:
            input_str = input("Enter a list of integers separated by spaces: ")
            nums = list(map(int, input_str.split()))
            return nums
        except ValueError:
            print(f"Invalid input. Please enter a valid list of integers. You have {3 - count} attempts left.")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def print_longest_consecutive_subsequence_length(length: int) -> None:
    """Prints the length of the longest consecutive subsequence."""
    if length == 0:
        print("\nThe input list is empty. There is no consecutive subsequence.")
    else:
        print(f"\nThe length of the longest consecutive subsequence is: {length}")

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_complexity() -> None:
    """Prints the time and space complexity of the algorithm."""
    print("\nTime Complexity: O(n) for the hash set approach, O(n log n) for the alternative approach.")
    print("Space Complexity: O(n) for the hash set approach, O(1) for the alternative approach if sorting is used.")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Longest Consecutive Subsequence Finder!")
    print("\nGoodbye!\n")

def main():
    """Main function to execute the longest consecutive subsequence finder."""
    print_welcome_message()
    try:
        
        approach = prompt_user_for_approach()
        nums = prompt_user_for_input()
        start_time = time.perf_counter()
        if approach == "hash":
            start_time = time.perf_counter()
            length = hash_longest_consecutive_subsequence_length(nums)
            end_time = time.perf_counter()
        else:
            start_time = time.perf_counter()
            length = alt_longest_consecutive_subsequence_length(nums)
            end_time = time.perf_counter()
        print_longest_consecutive_subsequence_length(length)
        print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        print_complexity()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print_thank_you_message()

if __name__ == "__main__":
    main()

# This program finds the length of the longest consecutive subsequence in an unsorted array of integers.
# It provides two approaches: one using a hash set and an alternative approach based on the size of the input list.
# The alternative approach will sort the list if it is small enough, or use a hash set for larger lists.


