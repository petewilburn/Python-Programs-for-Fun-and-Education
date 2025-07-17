# A Python program to solve the Word Break problem. 

# Minimum Python Version: 3.9

# --------------------------------------------------------------------------------------------------------------
# File: P3139_Word_Break.py
# Description: A Python program to determine if a string can be segmented into words from a given dictionary.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# --------------------------------------------------------------------------------------------------------------

import time

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Determines if the string s can be segmented into words from the dictionary wordDict.
        This optimized function uses dynamic programming with word-based iteration for better performance.
        
        For LeetCode submission: Remove the type checking lines below.
        :param s: The string to be segmented.
        :param wordDict: The dictionary of words.
        :return: True if the string can be segmented, False otherwise.
        """
        # Type checking - Remove these lines for LeetCode submission
        if not isinstance(s, str):
            raise TypeError("s must be a string")
        if not isinstance(wordDict, list):
            raise TypeError("wordDict must be a list")
        
        # Edge case handling
        if not s or not wordDict:
            return False
            
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can always be segmented
        
        # Optimized approach: iterate through words instead of all positions
        for i in range(1, n + 1):
            for word in word_set:
                word_len = len(word)
                if i >= word_len and dp[i - word_len] and s[i - word_len:i] == word:
                    dp[i] = True
                    break  # Early termination optimization
        
        return dp[n]

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Word Break Solver Program!")
        print("\nThis program will determine if a string can be segmented into words from a given dictionary.")
        print("You will be prompted to enter a string and a list of words.")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Word Break problem."""
        print("\nIntroduction:")
        print("The Word Break problem is a classic dynamic programming challenge that demonstrates")
        print("how to break down complex string problems into manageable subproblems.")
        print("\nReal-world applications:")
        print("- Text processing and natural language parsing")
        print("- Spell checkers and autocorrect systems")
        print("- URL parsing and domain validation")
        print("- Compound word analysis in linguistics")
        print("\nVisualization example:")
        print("String: 'leetcode' | Dictionary: ['leet', 'code']")
        print("```")
        print("  l e e t c o d e")
        print("  [----]         ← 'leet' found")
        print("        [-----]  ← 'code' found")
        print("```")
        print("Result: Can be segmented as 'leet' + 'code'")
        print("\nThis problem teaches optimal substructure and overlapping subproblems,")
        print("key concepts in dynamic programming algorithms.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Word Break problem."""
        print("\nProblem Statement:")
        print("Given a string s and a dictionary of words wordDict, determine if s can be")
        print("segmented into a space-separated sequence of one or more dictionary words.")
        print("\nConstraints:")
        print("- 1 ≤ s.length ≤ 300")
        print("- 1 ≤ wordDict.length ≤ 1000")
        print("- Dictionary words can be reused multiple times")
        print("- All strings contain only lowercase English letters")
        print("\nExamples:")
        print("1. s = 'leetcode', wordDict = ['leet', 'code']")
        print("   Output: True (can be segmented as 'leet code')")
        print("2. s = 'applepenapple', wordDict = ['apple', 'pen']")
        print("   Output: True (can be segmented as 'apple pen apple')")
        print("3. s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat']")
        print("   Output: False (no valid segmentation exists)")
        print("\nObjective: Return True if s can be segmented, False otherwise.")
        print("\nLet's get started!\n")

    @staticmethod
    def prompt_user_for_string() -> str:
        """Prompts the user for a string and returns it."""
        count = 0
        while count < 3:
            count += 1
            user_input = input("\nEnter a string to check if it can be segmented: ").strip()
            if user_input:
                return user_input
            else:
                print("Please enter a non-empty string.")
        raise ValueError("Too many invalid attempts. Exiting the program.")

    @staticmethod
    def prompt_user_for_word_dict() -> list[str]:
        """Prompts the user for a list of words and returns it."""
        count = 0
        while count < 3:
            count += 1
            words_input = input("\nEnter a list of words (comma-separated): ").strip()
            if words_input:
                words = [word.strip() for word in words_input.split(",") if word.strip()]
                if words:
                    return words
                else:
                    print("Please enter at least one valid word.")
            else:
                print("Please enter a non-empty list of words.")
        raise ValueError("Too many invalid attempts. Exiting the program.")
    
    @staticmethod
    def print_result(result: bool) -> None:
        """Prints the result of the Word Break problem."""
        if result:
            print("\nThe string can be segmented into words from the dictionary.")
        else:
            print("\nThe string cannot be segmented into words from the dictionary.")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the program in milliseconds."""
        print(f"\nRuntime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Word Break using Dynamic Programming")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Word Break problem."""
        print("\nIntuition:")
        print("Think of this problem as asking: 'Can I build this string using dictionary words as building blocks?'")
        print("\nKey insights:")
        print("1. **Optimal Substructure**: If I can segment s[0:i], and s[i:j] is a valid word,")
        print("   then I can segment s[0:j]")
        print("2. **Overlapping Subproblems**: The same substring positions are checked multiple times")
        print("3. **Bottom-up approach**: Build solutions from smaller subproblems")
        print("\nDP Table Visualization for 'leetcode' with ['leet', 'code']:")
        print("```")
        print("Position: 0  1  2  3  4  5  6  7  8")
        print("String:   '' l  e  e  t  c  o  d  e")
        print("DP:       T  F  F  F  T  F  F  F  T")
        print("          ↑           ↑           ↑")
        print("        empty      'leet'    'leetcode'")
        print("```")
        print("\nWhy DP works: Each position represents 'can segment up to here?'")
        print("We build the answer incrementally using previously computed results.")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach to solving the Word Break problem."""
        print("\nApproach (Optimized Word-Based DP):")
        print("1. **Preprocessing**: Convert wordDict to set for O(1) word lookups")
        print("2. **DP Initialization**: Create dp[0...n] where dp[i] = 'can segment s[0:i]?'")
        print("3. **Base Case**: dp[0] = True (empty string can always be segmented)")
        print("4. **State Transition**: For each position i (1 to n):")
        print("   - For each word in dictionary:")
        print("   - Check if word ends at position i and fits")
        print("   - If dp[i-word_length] is True and s[i-word_length:i] == word:")
        print("   - Then dp[i] = True (we found a valid segmentation)")
        print("5. **Early Termination**: Break as soon as we find one valid segmentation")
        print("6. **Result**: Return dp[n] (can we segment the entire string?)")
        print("\nWhy this optimization works:")
        print("- Traditional approach: O(n²) by checking all possible split points")
        print("- Our approach: O(n×m) by checking only dictionary words")
        print("- When m << n (small dictionary), this is significantly faster")
        print("- Real-world dictionaries are typically much smaller than input strings")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity of the Word Break solution."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n × m × L), where:")
        print("- n = string length")
        print("- m = dictionary size") 
        print("- L = average word length")
        print("\nDetailed Time Complexity Derivation:")
        print("1. Outer loop: iterate through each position i from 1 to n → O(n)")
        print("2. Inner loop: iterate through each word in dictionary → O(m)")
        print("3. String comparison s[i-word_len:i] == word takes O(L) time")
        print("4. DP lookup dp[i-word_len] is O(1)")
        print("5. Total: O(n) × O(m) × O(L) = O(n × m × L)")
        print("\nPractical Performance:")
        print("- Often performs as O(n × m) since L is typically small and constant")
        print("- When m << n (small dictionary), this beats O(n²) traditional DP")
        print("- Early termination with 'break' improves average-case performance")
        print("\nSpace Complexity: O(n + m)")
        print("\nSpace Complexity Breakdown:")
        print("- DP array: O(n) space for boolean values at each position")
        print("- Word set: O(m × L) space for storing dictionary (≈ O(m) for analysis)")
        print("- Temporary string slices: O(L) space per operation")
        print("- No recursive call stack (iterative solution)")
        print("- Total: O(n + m)")
        print("\nComparison with alternatives:")
        print("- Brute force: O(2^n) time - exponential, impractical")
        print("- Traditional DP: O(n² × L) time - worse when m << n")
        print("- Our optimized DP: O(n × m × L) - better for small dictionaries")

    @staticmethod
    def print_code() -> None:
        """Prints the code of the Word Break solution."""
        print("\nOptimized Solution with Type Checking (Educational Version):")
        print("    class Solution:")
        print("        def wordBreak(self, s: str, wordDict: list[str]) -> bool:")
        print("            # Type checking - Remove these lines for LeetCode submission")
        print("            if not isinstance(s, str):")
        print("                raise TypeError('s must be a string')")
        print("            if not isinstance(wordDict, list):")
        print("                raise TypeError('wordDict must be a list')")
        print("            ")
        print("            # Edge case handling")
        print("            if not s or not wordDict:")
        print("                return False")
        print("            ")
        print("            # Preprocessing: convert to set for O(1) lookups")
        print("            word_set = set(wordDict)")
        print("            n = len(s)")
        print("            ")
        print("            # DP initialization")
        print("            dp = [False] * (n + 1)")
        print("            dp[0] = True  # Base case: empty string")
        print("            ")
        print("            # Main DP loop - optimized word-based iteration")
        print("            for i in range(1, n + 1):")
        print("                for word in word_set:")
        print("                    word_len = len(word)")
        print("                    # Check if word fits and previous segment is valid")
        print("                    if (i >= word_len and ")
        print("                        dp[i - word_len] and ")
        print("                        s[i - word_len:i] == word):")
        print("                        dp[i] = True")
        print("                        break  # Early termination")
        print("            ")
        print("            return dp[n]")
        print()
        print("LeetCode Submission Version (Type Checking Removed):")
        print("    class Solution:")
        print("        def wordBreak(self, s: str, wordDict: List[str]) -> bool:")
        print("            if not s or not wordDict:")
        print("                return False")
        print("            word_set = set(wordDict)")
        print("            n = len(s)")
        print("            dp = [False] * (n + 1)")
        print("            dp[0] = True")
        print("            for i in range(1, n + 1):")
        print("                for word in word_set:")
        print("                    word_len = len(word)")
        print("                    if (i >= word_len and dp[i - word_len] and")
        print("                        s[i - word_len:i] == word):")
        print("                        dp[i] = True")
        print("                        break")
        print("            return dp[n]")
        print()
        print("Key Optimizations:")
        print("• Word-based iteration instead of position-based (better when dict is small)")
        print("• Early termination with break (stops as soon as valid segmentation found)")
        print("• Set-based word lookup (O(1) instead of O(m) linear search)")
        print("• Efficient string slicing (only for dictionary words, not all substrings)")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for using the Word Break solution!")

def main():
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()

    try:
        user_string = IO.prompt_user_for_string()
        user_word_dict = IO.prompt_user_for_word_dict()

        start_time = time.perf_counter()
        solution = Solution()
        result = solution.wordBreak(user_string, user_word_dict)
        end_time = time.perf_counter()

        IO.print_result(result)
        IO.print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        IO.print_solution_title()
        IO.print_intuition()
        IO.print_approach()
        IO.print_complexity()
        IO.print_code()
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        IO.print_thank_you_message()

if __name__ == "__main__":
    main()

# This code implements an optimized solution to the Word Break problem using dynamic programming.
# It uses word-based iteration for better performance when the dictionary is smaller than the string.
# The solution has a time complexity of O(n × m × L) and space complexity of O(n + m).
# The program includes comprehensive educational content with detailed complexity analysis.
# Type checking is included for educational use but can be easily removed for competitive programming.
# The solution demonstrates optimal substructure and overlapping subproblems in dynamic programming.