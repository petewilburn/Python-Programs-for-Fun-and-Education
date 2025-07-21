# A Python program to solve the Alien Dictionary problem using Topological Sort.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3269_Alien_Dictionary.py
# Description: A Python program to find the order of characters in an alien language.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

import time
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        Finds the order of characters in an alien language using topological sort.
        
        This educational version includes comprehensive error handling and detailed comments.
        Uses Kahn's algorithm for topological sorting with cycle detection.
        """
        if not words:
            return ""
        
        # Step 1: Build the graph and in-degree count
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # Step 2: Compare adjacent words to find character ordering
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            # Check for invalid case: word1 is prefix of word2 but longer
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""  # Invalid alien dictionary
            
            # Find the first different character
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Step 3: Topological sort using Kahn's algorithm
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            # Remove edges from current character
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for cycles (invalid alien dictionary)
        if len(result) != len(in_degree):
            return ""  # Cycle detected
        
        return ''.join(result)

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Alien Dictionary Program! 👽")
        print("This program uses topological sort to determine the order of characters")
        print("in an alien language from a list of sorted words.")
        print("\nLet's explore this fascinating graph algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Alien Dictionary problem."""
        print("\nIntroduction:")
        print("The Alien Dictionary problem is a classic graph algorithm challenge that demonstrates")
        print("the power of topological sorting in solving ordering problems.")
        print("\nReal-world applications:")
        print("- Compiler dependency resolution")
        print("- Task scheduling with prerequisites")
        print("- Academic course prerequisite ordering")
        print("- Package manager dependency resolution")
        print("- Build system dependency management")
        print("\nVisualization of alien language ordering:")
        print("```")
        print("Given words: ['wrt', 'wrf', 'er', 'ett', 'rftt']")
        print("Deduced order: w → e → r → t → f")
        print("```")
        print("From comparing adjacent words, we can determine character precedence.")
        print("\nTopological sort finds a linear ordering of characters where each character")
        print("appears before all characters that depend on it in the ordering.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Alien Dictionary problem."""
        print("\nProblem Statement:")
        print("Given a list of words from an alien language sorted lexicographically,")
        print("return the order of characters in the alien language.")
        print("\nDefinition:")
        print("The alien language uses lowercase English letters, but the order may differ")
        print("from standard English alphabetical order.")
        print("\nConstraints:")
        print("- 1 ≤ words.length ≤ 100")
        print("- 1 ≤ words[i].length ≤ 100")
        print("- words[i] consists of only lowercase English letters")
        print("- words are sorted lexicographically in alien language")
        print("\nExamples:")
        print("1. Input: ['wrt', 'wrf', 'er', 'ett', 'rftt']")
        print("   Output: 'wertf'")
        print("2. Input: ['z', 'x']")
        print("   Output: 'zx'")
        print("3. Input: ['z', 'x', 'z'] (Invalid case)")
        print("   Output: '' (empty string)")
        print("\nObjective: Return the lexicographical order, or empty string if invalid.")

    @staticmethod
    def prompt_for_input() -> list[str]:
        """Prompts the user to choose a test case and returns the corresponding word list."""
        print("\nChoose a test case:")
        print("1. Standard case: ['wrt', 'wrf', 'er', 'ett', 'rftt']")
        print("2. Simple case: ['z', 'x']")
        print("3. Complex case: ['z', 'z']")
        print("4. Invalid case: ['abc', 'ab']")
        print("5. Cycle case: ['z', 'x', 'z']")
        print("6. Single word: ['abcdef']")
        print("7. Empty input: []")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return IO.create_test_case(choice)
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid integer.")
    
    @staticmethod
    def create_test_case(choice: int) -> list[str]:
        """Creates a test case based on user choice."""
        if choice == 1:
            words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
            print("Created: ['wrt', 'wrf', 'er', 'ett', 'rftt']")
            return words
            
        elif choice == 2:
            words = ['z', 'x']
            print("Created: ['z', 'x']")
            return words
            
        elif choice == 3:
            words = ['z', 'z']
            print("Created: ['z', 'z']")
            return words
            
        elif choice == 4:
            words = ['abc', 'ab']
            print("Created: ['abc', 'ab'] (Invalid: longer word before shorter prefix)")
            return words
            
        elif choice == 5:
            words = ['z', 'x', 'z']
            print("Created: ['z', 'x', 'z'] (Invalid: inconsistent ordering)")
            return words
            
        elif choice == 6:
            words = ['abcdef']
            print("Created: ['abcdef'] (Single word)")
            return words
            
        elif choice == 7:
            words = []
            print("Created: [] (Empty input)")
            return words
        
        return []
    
    @staticmethod
    def print_result(result: str) -> None:
        """Prints the result of the alien dictionary ordering."""
        if result:
            print(f"\n✅ Result: '{result}'")
            print("Successfully determined the alien language character order!")
        else:
            print("\n❌ Result: '' (empty string)")
            print("Invalid alien dictionary - no valid ordering exists.")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Alien Dictionary using Topological Sort (Kahn's Algorithm)")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Alien Dictionary algorithm."""
        print("\nIntuition (Topological Sort for Alien Dictionary):")
        print("Think of this problem as finding dependencies between characters:")
        print("\n📊 Character Dependencies: A → B means A comes before B")
        print("🔄 Topological Sort: Orders nodes so dependencies are satisfied")
        print("\nKey insights:")
        print("1. **Word Comparison**: Adjacent words reveal character ordering")
        print("2. **Graph Building**: Create directed edges between characters")
        print("3. **Cycle Detection**: Cycles indicate invalid alien dictionary")
        print("4. **Topological Order**: Linear ordering respecting all dependencies")
        print("\nVisualization of the process:")
        print("```")
        print("Words: ['wrt', 'wrf', 'er', 'ett', 'rftt']")
        print("Compare 'wrt' vs 'wrf': t → f")
        print("Compare 'wrf' vs 'er':  w → e")
        print("Compare 'er' vs 'ett':  r → t")
        print("Compare 'ett' vs 'rftt': e → r")
        print("Graph: w → e → r → t → f")
        print("```")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the Alien Dictionary algorithm."""
        print("\nApproach (Topological Sort using Kahn's Algorithm):")
        print("1. **Build Graph**: Create directed graph from character dependencies")
        print("2. **Count In-degrees**: Track how many characters come before each character")
        print("3. **Find Starting Points**: Characters with in-degree 0 can be processed first")
        print("4. **Process Queue**: Remove characters with no dependencies, update neighbors")
        print("5. **Cycle Detection**: If not all characters processed, cycle exists")
        print("\nImplementation details:")
        print("• Use adjacency list representation for the graph")
        print("• Track in-degrees to identify processing order")
        print("• Queue processes characters in topological order")
        print("• Detect invalid cases: cycles and inconsistent prefixes")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of the Alien Dictionary algorithm."""
        print("\nAlien Dictionary Algorithm Implementation:")
        print("```python")
        print("def alienOrder(self, words: list[str]) -> str:")
        print("    if not words:")
        print("        return ''")
        print("    ")
        print("    # Build graph and in-degree count")
        print("    graph = defaultdict(set)")
        print("    in_degree = {char: 0 for word in words for char in word}")
        print("    ")
        print("    # Compare adjacent words")
        print("    for i in range(len(words) - 1):")
        print("        word1, word2 = words[i], words[i + 1]")
        print("        ")
        print("        # Check invalid prefix case")
        print("        if len(word1) > len(word2) and word1.startswith(word2):")
        print("            return ''")
        print("        ")
        print("        # Find first different character")
        print("        for j in range(min(len(word1), len(word2))):")
        print("            if word1[j] != word2[j]:")
        print("                if word2[j] not in graph[word1[j]]:")
        print("                    graph[word1[j]].add(word2[j])")
        print("                    in_degree[word2[j]] += 1")
        print("                break")
        print("    ")
        print("    # Topological sort using Kahn's algorithm")
        print("    queue = deque([char for char in in_degree if in_degree[char] == 0])")
        print("    result = []")
        print("    ")
        print("    while queue:")
        print("        char = queue.popleft()")
        print("        result.append(char)")
        print("        ")
        print("        for neighbor in graph[char]:")
        print("            in_degree[neighbor] -= 1")
        print("            if in_degree[neighbor] == 0:")
        print("                queue.append(neighbor)")
        print("    ")
        print("    # Check for cycles")
        print("    if len(result) != len(in_degree):")
        print("        return ''")
        print("    ")
        print("    return ''.join(result)")
        print("```")
        print("\nKey Implementation Details:")
        print("• Use defaultdict(set) to avoid duplicate edges")
        print("• Initialize in_degree for all characters present in words")
        print("• Handle invalid prefix case before building graph")
        print("• Use deque for efficient queue operations")
        print("• Check result length to detect cycles")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(C + N × M), where:")
        print("- C = total number of characters in all words")
        print("- N = number of words")
        print("- M = maximum word length")
        print("\nTime Complexity Derivation:")
        print("1. **Graph Building**: Compare N-1 adjacent word pairs → O(N × M)")
        print("2. **Character Processing**: Visit each character once → O(C)")
        print("3. **Topological Sort**: Process each character and edge once → O(C)")
        print("4. **Edge Processing**: Each edge processed once → O(min(C, N))")
        print("5. **Total**: O(C + N × M) - dominated by word comparison")
        print("\nMathematical Proof:")
        print("Let C = total characters, N = words, M = max word length, U = unique characters")
        print("\n**Phase 1: Graph Construction**")
        print("- Compare N-1 adjacent pairs, each taking O(M) time → O(N × M)")
        print("\n**Phase 2: Topological Sort (Kahn's Algorithm)**")
        print("- Process U characters and E edges, where E ≤ min(U², N-1)")
        print("- Time: O(U + E) ≤ O(U + U²) = O(U²)")
        print("- Since U ≤ 26 (alphabet) or U ≤ C, we have O(U²) ≤ O(C)")
        print("\n**Total Time Complexity:**")
        print("- T(n) = O(N × M) + O(C) = O(C + N × M)")
        print("- Proof: Both phases run independently, sum gives total complexity")
        print("\n**Optimality Analysis:**")
        print("- Must examine all C characters → Ω(C) lower bound")
        print("- Must compare adjacent words → Ω(N × M) lower bound")
        print("- Therefore: Ω(C + N × M) ≤ T(n) ≤ O(C + N × M)")
        print("- Conclusion: Algorithm is asymptotically optimal")
        print("\n**Practical Performance:**")
        print("- Typical case: C ≥ N × avg_length, so complexity ≈ O(C)")
        print("- Graph operations use efficient adjacency lists")
        print("- Early termination on invalid cases improves average performance")
        print("\nSpace Complexity: O(C)")
        print("\nSpace Complexity Breakdown:")
        print("- Graph adjacency lists: O(E) ≤ O(U²) space")
        print("- In-degree array: O(U) space")
        print("- Queue and result array: O(U) space each")
        print("- Total: O(U²) ≤ O(C) since U ≤ C")
        print("\nComparison with alternatives:")
        print("- DFS-based topological sort: O(C + N × M) time, O(C) space")
        print("- Brute force permutation: O(U! × C) time - exponential, impractical")
        print("- Hash-based cycle detection: O(C + N × M) time, O(C) space")
        print("- Our Kahn's algorithm: O(C + N × M) time, O(C) space - optimal")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Empty Word List**")
        print("   - Input: []")
        print("   - Handling: Return empty string immediately")
        print("   - Result: '' (no characters to order)")
        print("\n2. **Single Word**")
        print("   - Input: ['abcdef']")
        print("   - Handling: All characters have in-degree 0")
        print("   - Result: Any permutation (e.g., 'abcdef')")
        print("\n3. **Invalid Prefix Case**")
        print("   - Input: ['abc', 'ab']")
        print("   - Handling: Detect longer word before its prefix")
        print("   - Result: '' (invalid alien dictionary)")
        print("\n4. **Cycle Detection**")
        print("   - Input: ['z', 'x', 'z']")
        print("   - Handling: Topological sort detects cycle")
        print("   - Result: '' (inconsistent ordering)")
        print("\n5. **Identical Words**")
        print("   - Input: ['abc', 'abc']")
        print("   - Handling: No new ordering information")
        print("   - Result: Valid ordering (e.g., 'abc')")
        print("\n6. **Single Character Words**")
        print("   - Input: ['z', 'x', 'a']")
        print("   - Handling: Clear ordering from each comparison")
        print("   - Result: 'zxa'")
        print("\nRobustness Features:")
        print("✅ Handles all invalid alien dictionary cases")
        print("✅ Detects cycles and inconsistent orderings")
        print("✅ Efficient graph representation with sets")
        print("✅ Comprehensive edge case coverage")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring the Alien Dictionary Algorithm! 🎉")
        print("This solution demonstrates the power of topological sorting in solving")
        print("complex ordering problems with dependency constraints.")
        print("\nRemember: Graph algorithms can solve many real-world problems!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Alien Dictionary program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        words = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        result = solution.alienOrder(words)
        end_time = time.perf_counter()
        
        IO.print_result(result)
        IO.print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
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

# This program demonstrates topological sorting for solving the Alien Dictionary problem
# with optimal time complexity and comprehensive edge case handling.
# 
# Educational Features:
# - Comprehensive explanation of topological sorting algorithm
# - Visual demonstrations of graph building and character ordering
# - Multiple test cases covering all edge cases
# - Detailed complexity analysis with mathematical derivations
# - Real-world applications of dependency resolution
# - Interactive test case selection
# 
# Algorithm Highlights:
# - Time Complexity: O(C + N × M) - linear in total characters
# - Space Complexity: O(C) - efficient graph representation
# - Handles all invalid cases: cycles, inconsistent prefixes
# - Uses Kahn's algorithm for robust topological sorting
# 
# The program demonstrates how graph algorithms can elegantly solve complex
# ordering problems by modeling dependencies and using topological sort
# to find valid linear orderings. Perfect for understanding graph theory applications!
