# A Python program to solve the Longest Substring Without Repeating Characters problem using Sliding Window Technique.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3003_Longest_Substring_Without_Repeating_Characters.py
# Description: A Python program to find the length of the longest substring without repeating characters.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

import time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters using sliding window technique.
        
        This educational version includes comprehensive error handling and detailed comments.
        Uses the optimal sliding window approach with character index mapping.
        """
        if not s:
            return 0
        
        char_index_map = {}
        max_length = 0
        start = 0
        
        for index, char in enumerate(s):
            # If character exists and is within current window
            if char in char_index_map and char_index_map[char] >= start:
                # Move start to position after the duplicate
                start = char_index_map[char] + 1
            
            # Update character's latest index
            char_index_map[char] = index
            
            # Calculate current window length and update maximum
            current_length = index - start + 1
            max_length = max(max_length, current_length)
        
        return max_length

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Longest Substring Without Repeating Characters Program! 🔤")
        print("This program uses the sliding window technique to find the longest")
        print("substring without repeating characters in optimal time complexity.")
        print("\nLet's explore this elegant string optimization algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Longest Substring Without Repeating Characters problem."""
        print("\nIntroduction:")
        print("The Longest Substring Without Repeating Characters problem is a classic")
        print("string processing challenge that demonstrates the power of the sliding")
        print("window technique and efficient character tracking.")
        print("\nReal-world applications:")
        print("- Text processing and analysis systems")
        print("- Data deduplication algorithms")
        print("- Pattern recognition in genomics")
        print("- Cache optimization strategies")
        print("- Network packet analysis")
        print("- User input validation systems")
        print("\nThe sliding window technique efficiently maintains the longest")
        print("valid substring by expanding and contracting the window boundaries.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Longest Substring Without Repeating Characters problem."""
        print("\nProblem Statement:")
        print("Given a string s, find the length of the longest substring")
        print("without repeating characters.")
        print("\nDefinition:")
        print("A substring is a contiguous sequence of characters within a string.")
        print("No character should appear more than once in the valid substring.")
        print("\nConstraints:")
        print("- 0 ≤ s.length ≤ 5 × 10^4")
        print("- s consists of English letters, digits, symbols and spaces")
        print("- Case-sensitive: 'A' and 'a' are different characters")
        print("\nExamples:")
        print("1. Input: 'abcabcbb'")
        print("   Output: 3 (substring 'abc')")
        print("2. Input: 'bbbbb'")
        print("   Output: 1 (substring 'b')")
        print("3. Input: 'pwwkew'")
        print("   Output: 3 (substring 'wke')")
        print("4. Input: ''")
        print("   Output: 0 (empty string)")
        print("5. Input: 'au'")
        print("   Output: 2 (entire string)")
        print("\nObjective: Return the length of the longest substring without repeating characters.")

    @staticmethod
    def prompt_for_input() -> str:
        """Prompts the user to choose a test case and returns the corresponding string."""
        print("\nChoose a test case:")
        print("1. Standard case: 'abcabcbb'")
        print("2. All same characters: 'bbbbb'")
        print("3. Mixed pattern: 'pwwkew'")
        print("4. Empty string: ''")
        print("5. No duplicates: 'abcdef'")
        print("6. Single character: 'a'")
        print("7. Special characters: 'a!@#a'")
        print("8. Custom input")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-8): "))
                if 1 <= choice <= 8:
                    return IO.create_test_case(choice)
                else:
                    print("Please enter a number between 1 and 8.")
            except ValueError:
                print("Please enter a valid integer.")
    
    @staticmethod
    def create_test_case(choice: int) -> str:
        """Creates a test case based on user choice."""
        if choice == 1:
            test_string = "abcabcbb"
            print("Created: 'abcabcbb' - Expected length: 3")
            return test_string
            
        elif choice == 2:
            test_string = "bbbbb"
            print("Created: 'bbbbb' - Expected length: 1")
            return test_string
            
        elif choice == 3:
            test_string = "pwwkew"
            print("Created: 'pwwkew' - Expected length: 3")
            return test_string
            
        elif choice == 4:
            test_string = ""
            print("Created: '' (empty string) - Expected length: 0")
            return test_string
            
        elif choice == 5:
            test_string = "abcdef"
            print("Created: 'abcdef' - Expected length: 6")
            return test_string
            
        elif choice == 6:
            test_string = "a"
            print("Created: 'a' - Expected length: 1")
            return test_string
            
        elif choice == 7:
            test_string = "a!@#a"
            print("Created: 'a!@#a' - Expected length: 4")
            return test_string
            
        elif choice == 8:
            while True:
                try:
                    user_input = input("Enter a string: ")
                    print(f"Created: '{user_input}'")
                    return user_input
                except Exception:
                    print("Invalid input. Please try again.")
        
        return ""
    
    @staticmethod
    def print_result(length: int, test_string: str) -> None:
        """Prints the result of the longest substring calculation."""
        print(f"\n✅ Result: {length}")
        if test_string:
            print(f"Successfully found the longest substring length for '{test_string}'!")
        else:
            print("Successfully processed empty string!")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Longest Substring Without Repeating Characters using Sliding Window")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Longest Substring Without Repeating Characters algorithm."""
        print("\nIntuition (Sliding Window with Character Mapping):")
        print("Think of this problem as maintaining a dynamic window:")
        print("\n🪟 Sliding Window: Expand right, contract left when duplicates found")
        print("📍 Character Tracking: Remember last position of each character")
        print("🎯 Optimal Movement: Jump start pointer efficiently past duplicates")
        print("\nKey insights:")
        print("1. **Window Expansion**: Continuously expand the right boundary")
        print("2. **Duplicate Detection**: Use hashmap for O(1) character lookup")
        print("3. **Efficient Contraction**: Jump start pointer past duplicate")
        print("4. **Length Tracking**: Track maximum window size encountered")
        print("\nVisualization of algorithm steps:")
        print("```")
        print("String: 'abcabcbb'")
        print("")
        print("")
        print("Initial: abcabcbb →")
        print("- start = 0")
        print("- max length = 0")
        print("- map: {}")
        print("")
        print("Step 1: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("       |")
        print("      s,i")
        print("")
        print("[a]bcabcbb → ")
        print("    index = 0")
        print("    start = 0 ")
        print("    length = index - start + 1 = 1")
        print("    max length = 0 → max(0, 1) = 1")
        print("    map: {} → map: {a:0}")
        print("")
        print("Step 2: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("       | |")
        print("       s i")
        print("")
        print("[ab]cabcbb → ")
        print("    index = 1")
        print("    start = 0")
        print("    length = index - start + 1 = 2 ")
        print("    max length = max(1, 2) = 2")
        print("    map: {a:0, b:1}")
        print("")
        print("Step 3: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("       |   |")
        print("       s   i")
        print("")
        print("[abc]abcbb → ")
        print("    index = 2")
        print("    start = 0")
        print("    length = index - start + 1 = 3")
        print("    max length = max(2, 3) = 3")
        print("    map: {a:0, b:1, c:2}")
        print("")
        print("Step 4: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("         |   |")
        print("         s   i")
        print("")
        print("abc[a]bcbb → ")
        print("    index = 3")
        print("    duplicate 'a' found")
        print("        start = map[a] + 1 = 1")
        print("    length = index - start + 1 = 3")
        print("    max length = max(3, 3) = 3")
        print("    map: {a:3, b:1, c:2}")
        print("")
        print("Step 5: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("           |   |")
        print("           s   i")
        print("")
        print("abc[ab]cbb →")
        print("    index = 4")
        print("    duplicate 'b' found")
        print("        start = map[b] + 1 = 2")
        print("    length = index - start + 1 = 3")
        print("    max length = max(3, 3) = 3")
        print("    map: {a:3, b:4, c:2}")
        print("")
        print("Step 6: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("             |   |")
        print("             s   i")
        print("")
        print("abc[abc]bb →")
        print("    index = 5")
        print("    duplicate 'c' found")
        print("        start = map[c] + 1 = 3")
        print("    length = index - start + 1 = 3")
        print("    max length = max(3, 3) = 3")
        print("    map: {a:3, b:4, c:5}")
        print("")
        print("Step 7: ")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("                 | |")
        print("                 s i")
        print("")
        print("abcab[cb]b → ")
        print("    index = 6")
        print("    duplicate 'b' found")
        print("        start = map[b] + 1 = 5")
        print("    length = index - start + 1 = 2")
        print("    max length = max(3, 2) = 3")
        print("    map: {a:3, b:6, c:5}")
        print("")
        print("Step 8: ")
        print("")
        print("")
        print("index  0 1 2 3 4 5 6 7")
        print("char   a b c a b c b b")
        print("                     |")
        print("                    s,i")
        print("abcabc[b]b → ")
        print("    index = 7")
        print("    duplicate 'b' found")
        print("        start = map[b] + 1 = 7")
        print("        length = index - start + 1 = 1")
        print("    max length = max(3, 1) = 3")
        print("    map: {a:3, b:7, c:5}")
        print("")
        print("Maximum length found: 3")
        print("```")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the Longest Substring Without Repeating Characters algorithm."""
        print("\nApproach (Optimal Sliding Window with HashMap):")
        print("1. **Initialize Variables**: start pointer, character map, max length")
        print("2. **Iterate String**: Process each character with right pointer")
        print("3. **Check Duplicates**: Use hashmap to detect repeated characters")
        print("4. **Update Window**: Move start pointer past duplicate if found")
        print("5. **Track Maximum**: Update maximum length for current window")
        print("6. **Update Map**: Store current character's latest index")
        print("\nImplementation details:")
        print("• HashMap provides O(1) character lookup and storage")
        print("• Start pointer jumps efficiently past duplicates")
        print("• Window size = current_index - start_index + 1")
        print("• Only update start if duplicate is within current window")
        print("• Single pass through string achieves optimal complexity")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of the Longest Substring Without Repeating Characters algorithm."""
        print("\nLongest Substring Without Repeating Characters Algorithm Implementation:")
        print("```python")
        print("def lengthOfLongestSubstring(self, s: str) -> int:")
        print("    if not s:")
        print("        return 0")
        print("    ")
        print("    char_index_map = {}")
        print("    max_length = 0")
        print("    start = 0")
        print("    ")
        print("    for index, char in enumerate(s):")
        print("        # If character exists and is within current window")
        print("        if char in char_index_map and char_index_map[char] >= start:")
        print("            # Move start to position after the duplicate")
        print("            start = char_index_map[char] + 1")
        print("        ")
        print("        # Update character's latest index")
        print("        char_index_map[char] = index")
        print("        ")
        print("        # Calculate current window length and update maximum")
        print("        current_length = index - start + 1")
        print("        max_length = max(max_length, current_length)")
        print("    ")
        print("    return max_length")
        print("```")
        print("\nKey Implementation Details:")
        print("• HashMap stores most recent index of each character")
        print("• Check if duplicate is within current window (>= start)")
        print("• Start pointer jumps to position after duplicate character")
        print("• Update character index after processing duplicate logic")
        print("• Track maximum window size throughout iteration")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n), where:")
        print("- n = length of input string")
        print("\nTime Complexity Derivation:")
        print("1. **Single Pass**: Each character visited exactly once")
        print("2. **HashMap Operations**: O(1) average time for lookup/insertion")
        print("3. **Start Pointer Movement**: Moves at most n positions total")
        print("4. **Per Character Work**: Constant time operations")
        print("5. **Total**: O(n) characters × O(1) work = O(n)")
        print("\nMathematical Proof:")
        print("Let T(n) be the time to process string of length n")
        print("\n**Iteration Analysis:**")
        print("- Right pointer (index): moves from 0 to n-1 → exactly n steps")
        print("- Left pointer (start): moves from 0 to at most n-1 → at most n steps")
        print("- Total pointer movements: ≤ 2n")
        print("- HashMap operations: n lookups + n insertions = 2n operations")
        print("\n**Amortized Analysis:**")
        print("- Each character enters window once (right pointer)")
        print("- Each character leaves window at most once (left pointer)")
        print("- Total operations: O(n) + O(n) = O(n)")
        print("\nSpace Complexity: O(min(m, n)), where:")
        print("- m = size of character set (e.g., 128 for ASCII)")
        print("- n = length of input string")
        print("\nSpace Complexity Breakdown:")
        print("- HashMap storage: stores at most min(m, n) character-index pairs")
        print("- ASCII characters: at most 128 entries")
        print("- Unicode characters: potentially larger but bounded by string length")
        print("- Additional variables: O(1) space for pointers and counters")
        print("\nComparison with alternatives:")
        print("- Brute force (all substrings): O(n³) time - check every substring")
        print("- Nested loops with set: O(n²) time - sliding window per position")
        print("- Our sliding window: O(n) time, O(min(m,n)) space - optimal solution")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Empty String**")
        print("   - Input: '' (zero length)")
        print("   - Handling: Return 0 immediately")
        print("   - Result: 0")
        print("\n2. **Single Character**")
        print("   - Input: 'a' (one character)")
        print("   - Handling: No duplicates possible")
        print("   - Result: 1")
        print("\n3. **All Same Characters**")
        print("   - Input: 'aaaa' (repeated character)")
        print("   - Handling: Window size stays at 1")
        print("   - Result: 1")
        print("\n4. **No Repeating Characters**")
        print("   - Input: 'abcdef' (all unique)")
        print("   - Handling: Window expands to full string")
        print("   - Result: length of entire string")
        print("\n5. **Mixed Patterns**")
        print("   - Input: 'abba' (palindromic pattern)")
        print("   - Handling: Window contracts and expands appropriately")
        print("   - Result: 2 (substrings 'ab' or 'ba')")
        print("\n6. **Special Characters**")
        print("   - Input: 'a!@#$a' (symbols and letters)")
        print("   - Handling: Treats all characters equally")
        print("   - Result: 5 (substring '!@#$')")
        print("\n7. **Whitespace Characters**")
        print("   - Input: 'a b a' (spaces included)")
        print("   - Handling: Space is treated as valid character")
        print("   - Result: 2 (substrings 'a ' or ' b')")
        print("\nRobustness Features:")
        print("✅ Handles strings of any length including empty")
        print("✅ Works with all printable characters and Unicode")
        print("✅ Efficient memory usage with character set optimization")
        print("✅ Guaranteed to find optimal solution in single pass")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring the Longest Substring Without Repeating Characters Algorithm! 🎉")
        print("This solution demonstrates the power of the sliding window technique")
        print("and efficient character tracking in string processing problems.")
        print("\nRemember: Sometimes the best solution slides smoothly through the problem!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Longest Substring Without Repeating Characters program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        test_string = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        length = solution.lengthOfLongestSubstring(test_string)
        end_time = time.perf_counter()
        
        IO.print_result(length, test_string)
        IO.print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        IO.print_solution_title()
        IO.print_intuition()
        IO.print_approach()
        IO.print_code()
        IO.print_complexity()
        IO.print_edge_cases()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        IO.print_thank_you_message()

if __name__ == "__main__":
    main()

# This program demonstrates the sliding window technique for solving the Longest Substring
# Without Repeating Characters problem with optimal time complexity and comprehensive
# character handling.
# 
# Educational Features:
# - Comprehensive explanation of sliding window technique and character mapping
# - Visual demonstrations of window expansion/contraction and character tracking
# - Multiple test cases covering all edge cases and character types
# - Detailed complexity analysis with mathematical proofs
# - Real-world applications of string processing algorithms
# - Interactive test case selection with expected results
# 
# Algorithm Highlights:
# - Time Complexity: O(n) - single pass through string
# - Space Complexity: O(min(m, n)) - efficient character set handling
# - Sliding window technique with HashMap optimization
# - Handles all character types including Unicode
# 
# The program demonstrates how the sliding window technique elegantly solves
# string optimization problems by maintaining dynamic boundaries and using
# efficient data structures for character tracking. Perfect for understanding
# advanced string algorithms and optimization techniques!