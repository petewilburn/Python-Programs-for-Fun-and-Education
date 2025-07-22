# A Python program to solve the Container With Most Water problem using Two-Pointer Technique.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3011_Container_With_Most_Water.py
# Description: A Python program to find the maximum area of water that can be contained by two lines.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

import time

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Finds the maximum area of water that can be contained by two lines using two-pointer technique.
        
        This educational version includes comprehensive error handling and detailed comments.
        Uses the optimal two-pointer approach with greedy decision making.
        """
        if not height or len(height) < 2:
            return 0
        
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area (width × height)
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            
            # Update maximum area if current is better
            max_area = max(max_area, area)
            
            # Move the pointer with smaller height (greedy choice)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Container With Most Water Program! 🌊")
        print("This program uses the two-pointer technique to find the maximum area")
        print("of water that can be contained between two vertical lines.")
        print("\nLet's explore this elegant optimization algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Container With Most Water problem."""
        print("\nIntroduction:")
        print("The Container With Most Water problem is a classic optimization challenge")
        print("that demonstrates the power of the two-pointer technique and greedy algorithms.")
        print("\nReal-world applications:")
        print("- Water tank and reservoir design optimization")
        print("- Stock trading profit maximization")
        print("- Resource allocation in time intervals")
        print("- Manufacturing efficiency optimization")
        print("- Network bandwidth allocation")
        print("\nVisualization of water container:")
        print("```")
        print("Height: [1,8,6,2,5,4,8,3,7]")
        print(" Index:  0 1 2 3 4 5 6 7 8")
        print("")
        print("    8 |   █         █   ")
        print("    7 |   █         █   █")
        print("    6 |   █ █       █   █")
        print("    5 |   █ █   █   █   █")
        print("    4 |   █ █   █ █ █   █")
        print("    3 |   █ █   █ █ █ █ █")
        print("    2 |   █ █ █ █ █ █ █ █")
        print("    1 | █ █ █ █ █ █ █ █ █")
        print("    0 +─┴─┴─┴─┴─┴─┴─┴─┴─┴─")
        print("        0 1 2 3 4 5 6 7 8")
        print("```")
        print("Maximum area: Between indices 1 and 8 → Area = 7 × 7 = 49")
        print("\nThe two-pointer technique efficiently finds the optimal container")
        print("by making greedy decisions about which boundary to move.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Container With Most Water problem."""
        print("\nProblem Statement:")
        print("Given an integer array height of length n, where height[i] represents")
        print("the height of the i-th vertical line at position i on the x-axis.")
        print("\nDefinition:")
        print("Find two lines that, together with the x-axis, form a container")
        print("that can hold the maximum amount of water.")
        print("\nConstraints:")
        print("- 2 ≤ height.length ≤ 10^5")
        print("- 0 ≤ height[i] ≤ 10^4")
        print("- The container cannot be slanted")
        print("- Water level is determined by the shorter of the two lines")
        print("- Area = width × height = (j - i) × min(height[i], height[j])")
        print("\nExamples:")
        print("1. Input: [1,8,6,2,5,4,8,3,7]")
        print("   Output: 49 (between indices 1 and 8)")
        print("2. Input: [1,1]")
        print("   Output: 1 (only one possible container)")
        print("3. Input: [4,3,2,1,4]")
        print("   Output: 16 (between indices 0 and 4)")
        print("\nObjective: Return the maximum area of water the container can store.")

    @staticmethod
    def prompt_for_input() -> list[int]:
        """Prompts the user to choose a test case and returns the corresponding height array."""
        print("\nChoose a test case:")
        print("1. Standard case: [1,8,6,2,5,4,8,3,7]")
        print("2. Simple case: [1,1]")
        print("3. Symmetric case: [4,3,2,1,4]")
        print("4. Increasing heights: [1,2,3,4,5]")
        print("5. Decreasing heights: [5,4,3,2,1]")
        print("6. Large container: [1,8,100,2,100,4,8,3,7]")
        print("7. Custom input")
        
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
    def create_test_case(choice: int) -> list[int]:
        """Creates a test case based on user choice."""
        if choice == 1:
            heights = [1,8,6,2,5,4,8,3,7]
            print("Created: [1,8,6,2,5,4,8,3,7] - Expected max area: 49")
            return heights
            
        elif choice == 2:
            heights = [1,1]
            print("Created: [1,1] - Expected max area: 1")
            return heights
            
        elif choice == 3:
            heights = [4,3,2,1,4]
            print("Created: [4,3,2,1,4] - Expected max area: 16")
            return heights
            
        elif choice == 4:
            heights = [1,2,3,4,5]
            print("Created: [1,2,3,4,5] - Expected max area: 6")
            return heights
            
        elif choice == 5:
            heights = [5,4,3,2,1]
            print("Created: [5,4,3,2,1] - Expected max area: 6")
            return heights
            
        elif choice == 6:
            heights = [1,8,100,2,100,4,8,3,7]
            print("Created: [1,8,100,2,100,4,8,3,7] - Expected max area: 200")
            return heights
            
        elif choice == 7:
            while True:
                try:
                    user_input = input("Enter heights separated by spaces: ")
                    heights = list(map(int, user_input.split()))
                    if len(heights) < 2:
                        print("Please enter at least two heights.")
                        continue
                    print(f"Created: {heights}")
                    return heights
                except ValueError:
                    print("Invalid input. Please enter integers only.")
        
        return []
    
    @staticmethod
    def print_result(max_area: int) -> None:
        """Prints the result of the maximum area calculation."""
        print(f"\n✅ Result: {max_area}")
        print("Successfully found the maximum water container area!")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Container With Most Water using Two-Pointer Technique")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Container With Most Water algorithm."""
        print("\nIntuition (Two-Pointer Technique with Greedy Choice):")
        print("Think of this problem as finding the best water container:")
        print("\n🌊 Container Area: width × height (limited by shorter wall)")
        print("📏 Width Trade-off: Start wide, then trade width for potentially better height")
        print("🎯 Greedy Decision: Always move the pointer with the shorter height")
        print("\nKey insights:")
        print("1. **Maximum Width Start**: Begin with widest possible container")
        print("2. **Height Limitation**: Water level = min(left_height, right_height)")
        print("3. **Optimal Movement**: Moving shorter wall might find taller wall")
        print("4. **Guaranteed Optimality**: Never miss the best solution")
        print("\nVisualization of pointer movement:")
        print("```")
        print("Heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("Initial:  ↑                       ↑")
        print("         left                   right")
        print("Area = min(1,7) × 8 = 8")
        print("Max Area = 8")
        print("")
        print("Move left (height[left]=1 < height[right]=7):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑                    ↑")
        print("           left                 right")
        print("Area = min(8,7) × 7 = 49")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 > height[right]=7):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑                 ↑")
        print("           left              right")
        print("Area = min(8,3) × 6 = 18")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 > height[right]=3):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑              ↑")
        print("           left           right")
        print("Area = min(8,8) × 5 = 40")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 = height[right]=8):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑           ↑")
        print("           left        right")
        print("Area = min(8,4) × 4 = 16")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 > height[right]=4):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑        ↑")
        print("           left     right")
        print("Area = min(8,5) × 3 = 15")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 > height[right]=5):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑     ↑")
        print("           left  right")
        print("Area = min(8,2) × 2 = 4")
        print("Max Area = 49")
        print("")
        print("Move right (height[left]=8 > height[right]=2):")
        print("         [1, 8, 6, 2, 5, 4, 8, 3, 7]")
        print("             ↑  ↑")
        print("           left right")
        print("Area = min(8,6) × 1 = 6")
        print("Max Area = 49")
        print("```")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the Container With Most Water algorithm."""
        print("\nApproach (Optimal Two-Pointer with Greedy Strategy):")
        print("1. **Initialize Pointers**: left = 0, right = n-1 (maximum width)")
        print("2. **Calculate Area**: area = min(height[left], height[right]) × (right - left)")
        print("3. **Update Maximum**: track the best area found so far")
        print("4. **Greedy Move**: move the pointer with the smaller height inward")
        print("5. **Repeat**: continue until pointers meet")
        print("\nImplementation details:")
        print("• Start with maximum possible width for optimal exploration")
        print("• Use min() to find the limiting height (water spills over shorter wall)")
        print("• Greedy choice: moving shorter wall might improve height")
        print("• Moving taller wall guarantees no improvement (width decreases, height can't increase)")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of the Container With Most Water algorithm."""
        print("\nContainer With Most Water Algorithm Implementation:")
        print("```python")
        print("def maxArea(self, height: list[int]) -> int:")
        print("    if not height or len(height) < 2:")
        print("        return 0")
        print("    ")
        print("    left, right = 0, len(height) - 1")
        print("    max_area = 0")
        print("    ")
        print("    while left < right:")
        print("        # Calculate current area")
        print("        width = right - left")
        print("        current_height = min(height[left], height[right])")
        print("        area = width * current_height")
        print("        ")
        print("        # Update maximum area")
        print("        max_area = max(max_area, area)")
        print("        ")
        print("        # Move pointer with smaller height (greedy choice)")
        print("        if height[left] < height[right]:")
        print("            left += 1")
        print("        else:")
        print("            right -= 1")
        print("    ")
        print("    return max_area")
        print("```")
        print("\nKey Implementation Details:")
        print("• Two pointers start at opposite ends for maximum initial width")
        print("• Area calculation: width × min(heights) for water physics")
        print("• Greedy decision ensures we explore all potentially optimal solutions")
        print("• Single pass through array achieves O(n) time complexity")
        print("• No additional space needed beyond pointer variables")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n), where:")
        print("- n = number of vertical lines (length of height array)")
        print("\nTime Complexity Derivation:")
        print("1. **Single Pass**: Each element visited at most once by each pointer")
        print("2. **Pointer Movement**: In each iteration, exactly one pointer moves inward")
        print("3. **Total Iterations**: At most n-1 iterations (when pointers meet)")
        print("4. **Per Iteration Work**: Constant time operations → O(1)")
        print("5. **Total**: O(n) iterations × O(1) work = O(n)")
        print("\nMathematical Proof:")
        print("Let T(n) be the time to process array of length n")
        print("\n**Iteration Analysis:**")
        print("- Initial state: left = 0, right = n-1")
        print("- Each iteration: left increases OR right decreases (never both)")
        print("- Terminal state: left ≥ right")
        print("- Maximum iterations: (n-1) + 0 = n-1")
        print("\n**Optimality Proof:**")
        print("- Must consider each position as potential container boundary → Ω(n)")
        print("- Our algorithm visits each position at most once → O(n)")
        print("- Greedy choice guarantees no optimal solution is missed")
        print("- Therefore: T(n) = Θ(n) - optimal for this problem")
        print("\n**Greedy Choice Correctness:**")
        print("- Moving taller wall: width↓, height≤ → area can only decrease")
        print("- Moving shorter wall: width↓, height≤ → area might increase")
        print("- By always moving shorter wall, we explore all improvements")
        print("\nSpace Complexity: O(1)")
        print("\nSpace Complexity Breakdown:")
        print("- Two pointer variables: O(1) space")
        print("- Maximum area tracking: O(1) space")
        print("- No additional data structures needed")
        print("- Memory usage independent of input size")
        print("\nComparison with alternatives:")
        print("- Brute force (all pairs): O(n²) time - check every pair")
        print("- Dynamic programming: O(n²) time, O(n²) space - overkill")
        print("- Our two-pointer: O(n) time, O(1) space - optimal solution")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Minimum Array Length**")
        print("   - Input: [a, b] (exactly two elements)")
        print("   - Handling: Direct calculation, no iteration needed")
        print("   - Result: min(a, b) × 1")
        print("\n2. **Equal Heights**")
        print("   - Input: [5, 5, 5, 5] (all same height)")
        print("   - Handling: Algorithm works normally, finds maximum width")
        print("   - Result: 5 × 3 = 15 (maximum width with same height)")
        print("\n3. **Strictly Increasing**")
        print("   - Input: [1, 2, 3, 4, 5] (ascending order)")
        print("   - Handling: Left pointer moves first (smaller heights)")
        print("   - Result: Often involves endpoints for maximum width")
        print("\n4. **Strictly Decreasing**")
        print("   - Input: [5, 4, 3, 2, 1] (descending order)")
        print("   - Handling: Right pointer moves first (smaller heights)")
        print("   - Result: Similar to increasing case, endpoints important")
        print("\n5. **Single Peak**")
        print("   - Input: [1, 5, 1] (peak in middle)")
        print("   - Handling: Pointers converge toward peak")
        print("   - Result: Peak often involved in optimal solution")
        print("\n6. **Large Values**")
        print("   - Input: Arrays with height[i] up to 10^4")
        print("   - Handling: Algorithm handles large numbers efficiently")
        print("   - Result: No overflow issues with modern integer types")
        print("\nRobustness Features:")
        print("✅ Handles arrays of any length ≥ 2")
        print("✅ Works efficiently with all height distributions")
        print("✅ Guaranteed to find optimal solution in single pass")
        print("✅ No risk of infinite loops or stack overflow")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring the Container With Most Water Algorithm! 🎉")
        print("This solution demonstrates the power of the two-pointer technique")
        print("and greedy algorithms in solving optimization problems efficiently.")
        print("\nRemember: Sometimes the optimal strategy is to be greedy!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Container With Most Water program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        heights = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        max_area = solution.maxArea(heights)
        end_time = time.perf_counter()
        
        IO.print_result(max_area)
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

# This program demonstrates the two-pointer technique for solving the Container With Most Water
# problem with optimal time complexity and comprehensive edge case handling.
# 
# Educational Features:
# - Comprehensive explanation of two-pointer technique and greedy algorithms
# - Visual demonstrations of container area calculation and pointer movement
# - Multiple test cases covering all edge cases and height distributions
# - Detailed complexity analysis with mathematical proofs
# - Real-world applications of optimization problems
# - Interactive test case selection with expected results
# 
# Algorithm Highlights:
# - Time Complexity: O(n) - single pass through array
# - Space Complexity: O(1) - constant space usage
# - Greedy decision making ensures optimal solution
# - Two-pointer technique maximizes efficiency
# 
# The program demonstrates how simple greedy strategies can elegantly solve
# complex optimization problems by making locally optimal choices that
# lead to globally optimal solutions. Perfect for understanding optimization!