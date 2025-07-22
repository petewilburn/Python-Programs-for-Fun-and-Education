# A Python program to solve the Longest Palindromic Substring problem using Center Expansion Technique.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3005_Longest_Palindromic_Substring.py
# Description: A Python program to find the longest palindromic substring in a given string.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring using center expansion technique.
        
        This educational version includes comprehensive error handling and detailed comments.
        Uses the optimal center expansion approach for both odd and even length palindromes.
        """
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        def expand_around_center(left: int, right: int) -> int:
            """Expands around center and returns the length of palindrome."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Check for odd length palindromes (center at i)
            len1 = expand_around_center(i, i)
            
            # Check for even length palindromes (center between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            # Get maximum length palindrome centered at current position
            current_max = max(len1, len2)
            
            # Update global maximum if current palindrome is longer
            if current_max > max_length:
                max_length = current_max
                start = i - (current_max - 1) // 2
        
        return s[start:start + max_length]

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Longest Palindromic Substring Program! 🔄")
        print("This program uses the center expansion technique to find the longest")
        print("palindromic substring in optimal time complexity.")
        print("\nLet's explore this elegant string analysis algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Longest Palindromic Substring problem."""
        print("\nIntroduction:")
        print("The Longest Palindromic Substring problem is a classic string processing")
        print("challenge that demonstrates the power of the center expansion technique")
        print("and efficient palindrome detection algorithms.")
        print("\nReal-world applications:")
        print("- DNA sequence analysis and bioinformatics")
        print("- Text processing and linguistic analysis")
        print("- Data compression algorithms")
        print("- Pattern recognition in genomics")
        print("- Cryptographic applications")
        print("- Natural language processing")
        print("\nThe center expansion technique efficiently finds palindromes")
        print("by expanding outward from each possible center position.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Longest Palindromic Substring problem."""
        print("\nProblem Statement:")
        print("Given a string s, return the longest palindromic substring in s.")
        print("\nDefinition:")
        print("A palindrome is a string that reads the same backward as forward.")
        print("A substring is a contiguous sequence of characters within a string.")
        print("\nConstraints:")
        print("- 1 ≤ s.length ≤ 1000")
        print("- s consists of only digits and English letters")
        print("- Case-sensitive: 'A' and 'a' are different characters")
        print("\nExamples:")
        print("1. Input: 'babad'")
        print("   Output: 'bab' or 'aba' (both are valid)")
        print("2. Input: 'cbbd'")
        print("   Output: 'bb' (even length palindrome)")
        print("3. Input: 'racecar'")
        print("   Output: 'racecar' (entire string)")
        print("4. Input: 'a'")
        print("   Output: 'a' (single character)")
        print("5. Input: 'ac'")
        print("   Output: 'a' or 'c' (no longer palindrome)")
        print("\nObjective: Return the longest palindromic substring in the given string.")

    @staticmethod
    def prompt_for_input() -> str:
        """Prompts the user to choose a test case and returns the corresponding string."""
        print("\nChoose a test case:")
        print("1. Standard case: 'babad'")
        print("2. Even palindrome: 'cbbd'")
        print("3. Full palindrome: 'racecar'")
        print("4. Single character: 'a'")
        print("5. No long palindrome: 'abcdef'")
        print("6. Mixed case: 'Aa'")
        print("7. Repeated pattern: 'aabaa'")
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
            test_string = "babad"
            print("Created: 'babad' - Expected: 'bab' or 'aba'")
            return test_string
            
        elif choice == 2:
            test_string = "cbbd"
            print("Created: 'cbbd' - Expected: 'bb'")
            return test_string
            
        elif choice == 3:
            test_string = "racecar"
            print("Created: 'racecar' - Expected: 'racecar'")
            return test_string
            
        elif choice == 4:
            test_string = "a"
            print("Created: 'a' - Expected: 'a'")
            return test_string
            
        elif choice == 5:
            test_string = "abcdef"
            print("Created: 'abcdef' - Expected: any single character")
            return test_string
            
        elif choice == 6:
            test_string = "Aa"
            print("Created: 'Aa' - Expected: 'A' or 'a'")
            return test_string
            
        elif choice == 7:
            test_string = "aabaa"
            print("Created: 'aabaa' - Expected: 'aabaa'")
            return test_string
            
        elif choice == 8:
            while True:
                try:
                    user_input = input("Enter a string: ")
                    if user_input:
                        print(f"Created: '{user_input}'")
                        return user_input
                    else:
                        print("Please enter a non-empty string.")
                except Exception:
                    print("Invalid input. Please try again.")
        
        return ""
    
    @staticmethod
    def print_result(palindrome: str, test_string: str) -> None:
        """Prints the result of the longest palindromic substring calculation."""
        print(f"\n✅ Result: '{palindrome}'")
        print(f"Successfully found the longest palindromic substring in '{test_string}'!")
        print(f"Length: {len(palindrome)}")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Longest Palindromic Substring using Center Expansion")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Longest Palindromic Substring algorithm."""
        print("\nIntuition (Center Expansion with Odd/Even Handling):")
        print("Think of this problem as finding symmetric patterns:")
        print("\n🎯 Center Expansion: Expand outward from each possible center")
        print("🔄 Symmetry Check: Compare characters on both sides")
        print("📏 Length Tracking: Track the longest palindrome found")
        print("\nKey insights:")
        print("1. **Every Position as Center**: Each character can be a palindrome center")
        print("2. **Two Types of Centers**: Odd length (at character) and even length (between characters)")
        print("3. **Expansion Strategy**: Grow outward while maintaining symmetry")
        print("4. **Optimal Tracking**: Remember the longest palindrome encountered")
        print("\nVisualization of center expansion process:")
        print("```")
        print("String: 'babad'")
        print("Index:   01234")
        print("")
        print("Center 0 (odd): [b]abad → length: 1")
        print("Center 0-1 (even): [ba]bad → no palindrome")
        print("")
        print("Center 1 (odd):")
        print("  Start: b[a]bad")
        print("  Expand: [bab]ad → palindrome! length: 3")
        print("  Try expand: [babad] → no match")
        print("")
        print("Center 2 (odd): ba[b]ad → length: 1")
        print("Center 2-3 (even): bab[ad] → no palindrome")
        print("")
        print("Center 3 (odd):")
        print("  Start: bab[a]d")
        print("  Expand: ba[bad] → palindrome! length: 3")
        print("")
        print("Center 4 (odd): baba[d] → length: 1")
        print("")
        print("Best palindromes found: 'bab' and 'aba' (both length 3)")
        print("Algorithm returns first one found: 'bab'")
        print("```")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the Longest Palindromic Substring algorithm."""
        print("\nApproach (Optimal Center Expansion with Dual Check):")
        print("1. **Initialize Variables**: start position and maximum length")
        print("2. **Iterate Centers**: Check each position as potential center")
        print("3. **Odd Length Check**: Expand around single character center")
        print("4. **Even Length Check**: Expand around character pair center")
        print("5. **Length Comparison**: Take maximum of odd and even expansions")
        print("6. **Update Global**: Track the longest palindrome found")
        print("7. **Extract Result**: Return substring using start and length")
        print("\nImplementation details:")
        print("• Center expansion stops when characters don't match or bounds exceeded")
        print("• Start position calculated using center and palindrome length")
        print("• Both odd and even palindromes checked at each position")
        print("• Length calculation: right - left - 1 after expansion stops")
        print("• Start index: center - (length - 1) // 2 for proper alignment")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of the Longest Palindromic Substring algorithm."""
        print("\nLongest Palindromic Substring Algorithm Implementation:")
        print("```python")
        print("def longestPalindrome(self, s: str) -> str:")
        print("    if not s:")
        print("        return \"\"")
        print("    ")
        print("    start = 0")
        print("    max_length = 1")
        print("    ")
        print("    def expand_around_center(left: int, right: int) -> int:")
        print("        while left >= 0 and right < len(s) and s[left] == s[right]:")
        print("            left -= 1")
        print("            right += 1")
        print("        return right - left - 1")
        print("    ")
        print("    for i in range(len(s)):")
        print("        # Check for odd length palindromes (center at i)")
        print("        len1 = expand_around_center(i, i)")
        print("        ")
        print("        # Check for even length palindromes (center between i and i+1)")
        print("        len2 = expand_around_center(i, i + 1)")
        print("        ")
        print("        # Get maximum length palindrome centered at current position")
        print("        current_max = max(len1, len2)")
        print("        ")
        print("        # Update global maximum if current palindrome is longer")
        print("        if current_max > max_length:")
        print("            max_length = current_max")
        print("            start = i - (current_max - 1) // 2")
        print("    ")
        print("    return s[start:start + max_length]")
        print("```")
        print("\nKey Implementation Details:")
        print("• expand_around_center handles both odd and even expansion cases")
        print("• Length calculation accounts for over-expansion by subtracting 1")
        print("• Start position uses integer division for proper center alignment")
        print("• Two separate calls handle odd-length and even-length palindromes")
        print("• Global tracking ensures we return the longest palindrome found")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n²), where:")
        print("- n = length of input string")
        print("\nTime Complexity Derivation:")
        print("1. **Outer Loop**: Iterates through n possible centers")
        print("2. **Center Expansion**: Each expansion takes O(n) time in worst case")
        print("3. **Two Checks**: Odd and even length checks per center")
        print("4. **Total Operations**: n centers × O(n) expansion = O(n²)")
        print("\nMathematical Proof:")
        print("Let T(n) be the time to process string of length n")
        print("\n**Worst Case Analysis:**")
        print("- Best case: No palindromes longer than 1 → O(n)")
        print("- Average case: Some palindromes of moderate length → O(n²)")
        print("- Worst case: Entire string is palindrome → O(n²)")
        print("\n**Expansion Analysis:**")
        print("- Each center can expand at most n/2 positions in each direction")
        print("- Total expansions across all centers: ∑(expansion_i) ≤ n²")
        print("- Therefore: T(n) = O(n²)")
        print("\nSpace Complexity: O(1)")
        print("\nSpace Complexity Breakdown:")
        print("- Start position and max length: O(1) space")
        print("- Expansion function variables: O(1) space")
        print("- No additional data structures needed")
        print("- Memory usage independent of input size")
        print("\nComparison with alternatives:")
        print("- Brute force (check all substrings): O(n³) time")
        print("- Dynamic programming: O(n²) time, O(n²) space")
        print("- Manacher's algorithm: O(n) time, O(n) space - most optimal")
        print("- Our center expansion: O(n²) time, O(1) space - good balance")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Single Character**")
        print("   - Input: 'a' (length 1)")
        print("   - Handling: Trivially a palindrome")
        print("   - Result: 'a'")
        print("\n2. **Two Characters - Same**")
        print("   - Input: 'aa' (repeated character)")
        print("   - Handling: Even-length palindrome detected")
        print("   - Result: 'aa'")
        print("\n3. **Two Characters - Different**")
        print("   - Input: 'ab' (no palindrome)")
        print("   - Handling: Returns first character")
        print("   - Result: 'a'")
        print("\n4. **Entire String Palindrome**")
        print("   - Input: 'racecar' (full palindrome)")
        print("   - Handling: Center expansion covers entire string")
        print("   - Result: 'racecar'")
        print("\n5. **No Long Palindromes**")
        print("   - Input: 'abcdef' (all unique)")
        print("   - Handling: Each character is length-1 palindrome")
        print("   - Result: 'a' (first character)")
        print("\n6. **Multiple Equal Length**")
        print("   - Input: 'abacabad' (multiple 3-length palindromes)")
        print("   - Handling: Returns first longest palindrome found")
        print("   - Result: 'aba'")
        print("\n7. **Case Sensitivity**")
        print("   - Input: 'Aa' (different cases)")
        print("   - Handling: Treats as different characters")
        print("   - Result: 'A' or 'a'")
        print("\nRobustness Features:")
        print("✅ Handles strings of any length ≥ 1")
        print("✅ Works with all ASCII characters including symbols")
        print("✅ Correctly identifies both odd and even length palindromes")
        print("✅ Guaranteed to find optimal solution")
        print("✅ No risk of infinite loops or memory issues")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring the Longest Palindromic Substring Algorithm! 🎉")
        print("This solution demonstrates the power of the center expansion technique")
        print("and efficient palindrome detection in string processing problems.")
        print("\nRemember: Sometimes the best patterns are symmetric!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Longest Palindromic Substring program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        test_string = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        palindrome = solution.longestPalindrome(test_string)
        end_time = time.perf_counter()
        
        IO.print_result(palindrome, test_string)
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

# This program demonstrates the center expansion technique for solving the Longest Palindromic
# Substring problem with optimal space complexity and comprehensive palindrome handling.
# 
# Educational Features:
# - Comprehensive explanation of center expansion technique and palindrome detection
# - Visual demonstrations of odd/even length palindrome expansion
# - Multiple test cases covering all edge cases and palindrome types
# - Detailed complexity analysis with mathematical proofs
# - Real-world applications of string analysis algorithms
# - Interactive test case selection with expected results
# 
# Algorithm Highlights:
# - Time Complexity: O(n²) - optimal for center expansion approach
# - Space Complexity: O(1) - constant space usage
# - Center expansion technique handles both odd and even palindromes
# - Handles all ASCII characters and case sensitivity
# 
# The program demonstrates how the center expansion technique elegantly solves
# palindrome detection problems by systematically checking each possible center
# and expanding outward while maintaining symmetry. Perfect for understanding
# string analysis algorithms and pattern recognition techniques!
