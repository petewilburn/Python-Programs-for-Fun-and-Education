# A Python program to solve the 3Sum problem using a two-pointer approach.

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3015_3Sum.py
# Description: A Python program to solve the 3Sum problem, which finds all unique triplets in an array
# that sum to zero.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import time

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        """
        Finds all unique triplets in the array that sum to zero.
        Optimized version with comprehensive type checking for educational use.
        For LeetCode submission: Remove the type checking section (marked below).
        
        Time Complexity: O(n^2) where n is the length of nums
        Space Complexity: O(1) auxiliary space, O(k) for output where k is number of triplets
        
        :param nums: List of integers
        :return: List of unique triplets that sum to zero
        """
        # === TYPE CHECKING SECTION - REMOVE FOR LEETCODE SUBMISSION ===
        if not isinstance(nums, list):
            raise TypeError("nums must be a list")
        if not all(isinstance(num, int) for num in nums):
            raise TypeError("All elements in nums must be integers")
        # === END TYPE CHECKING SECTION ===
        
        # Early termination for edge cases
        if len(nums) < 3:
            return []
        
        nums.sort()  # Sort for two-pointer technique and duplicate handling
        result = []
        n = len(nums)
        
        # Optimization: early exit if smallest number > 0 or largest < 0
        if nums[0] > 0 or nums[n-1] < 0:
            return []
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: if current number > 0, no valid triplets possible
            if nums[i] > 0:
                break
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for both pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
        
        return result
    
class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the 3Sum Finder Program!")
        print("\nThis program will find all unique triplets in an array that sum to zero.")
        print("You will be prompted to enter a list of integers.")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the 3Sum problem."""
        print("\nIntroduction:")
        print("The 3Sum problem is a fundamental algorithmic challenge that demonstrates the power of")
        print("sorting combined with the two-pointer technique. It's a classic example of how we can")
        print("optimize from a brute force O(n³) solution to an elegant O(n²) approach.")
        print()
        print("Real-world applications:")
        print("• Financial analysis: Finding transactions that balance to zero")
        print("• Chemistry: Balancing chemical equations with three components")
        print("• Game theory: Finding equilibrium points in three-player scenarios")
        print("• Data analysis: Identifying triplets of features with specific relationships")
        print()
        print("This problem serves as an excellent foundation for understanding:")
        print("• Two-pointer technique optimization")
        print("• Duplicate handling in sorted arrays")
        print("• Time-space complexity trade-offs")
        print("• LeetCode-style algorithmic problem solving")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the 3Sum problem."""
        print("\nProblem Statement:")
        print("Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]")
        print("such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] = 0.")
        print()
        print("Key Constraints:")
        print("• 3 ≤ nums.length ≤ 3000")
        print("• -10⁵ ≤ nums[i] ≤ 10⁵")
        print("• The solution set must not contain duplicate triplets")
        print("• Order of triplets in the result doesn't matter")
        print("• Elements within each triplet should be in non-decreasing order")
        print()
        print("Examples:")
        print("Input:  nums = [-1, 0, 1, 2, -1, -4]")
        print("Output: [[-1, -1, 2], [-1, 0, 1]]")
        print("Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0")
        print("             nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0")
        print()
        print("Input:  nums = [0, 1, 1]")
        print("Output: []")
        print("Explanation: The only possible triplet does not sum up to 0")
        print()
        print("Input:  nums = [0, 0, 0]")
        print("Output: [[0, 0, 0]]")
        print("Explanation: The only possible triplet sums up to 0")

    @staticmethod
    def prompt_user_for_numbers() -> list[int]:
        """Prompts the user for a list of integers and returns it."""
        count = 0
        while count < 3:
            count += 1
            user_input = input("Enter a list of integers separated by spaces: ")
            try:
                numbers = list(map(int, user_input.split()))
                if len(numbers) < 3:
                    print("Please enter at least 3 integers to find triplets.")
                    continue
                return numbers
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        raise ValueError("Too many invalid attempts. Exiting the program.")
    
    @staticmethod
    def print_triplets(triplets: list[list[int]]) -> None:
        """Prints the unique triplets found."""
        if not triplets:
            print("\nNo unique triplets found that sum to zero.")
        else:
            print("\nUnique triplets that sum to zero:")
            for triplet in triplets:
                print(triplet)

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the program in milliseconds."""
        print(f"\nRuntime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution Title: 3Sum Problem using Two-Pointer Approach")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the algorithm."""
        print("\nIntuition:")
        print("Think of this problem as: 'For each number, can I find two other numbers that")
        print("complete the equation a + b + c = 0?'")
        print()
        print("Key insights:")
        print("1. **Sorting enables two-pointer technique**: Once sorted, we can use the fact that")
        print("   moving the left pointer increases the sum, moving right pointer decreases it.")
        print()
        print("2. **Fix one element, find the other two**: For each nums[i], we need to find")
        print("   nums[j] and nums[k] such that nums[i] + nums[j] + nums[k] = 0")
        print("   This reduces the problem from 3Sum to 2Sum!")
        print()
        print("3. **Duplicate elimination**: Sorting helps us skip duplicate values efficiently")
        print("   by comparing adjacent elements.")
        print()
        print("Visual example with [-4, -1, -1, 0, 1, 2]:")
        print("```")
        print("i=0, nums[i]=-4: Find two numbers that sum to +4")
        print("  left=1(-1), right=5(2): -1 + 2 = 1 < 4 → move left")
        print("  left=2(-1), right=5(2): -1 + 2 = 1 < 4 → move left")
        print("  left=3(0),  right=5(2): 0 + 2 = 2 < 4 → move left")
        print("  left=4(1),  right=5(2): 1 + 2 = 3 < 4 → move left")
        print("  left > right → no solution for nums[i]=-4")
        print("```")
        print()
        print("This approach transforms O(n³) brute force into O(n²) optimized solution!")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used to solve the problem."""
        print("\nApproach (Optimized Two-Pointer with Early Termination):")
        print()
        print("1. **Preprocessing & Validation**:")
        print("   • Validate input types (educational version)")
        print("   • Return [] if len(nums) < 3")
        print("   • Sort the array: enables two-pointer technique and duplicate skipping")
        print()
        print("2. **Early Optimization Checks**:")
        print("   • If nums[0] > 0: all numbers positive → impossible to sum to 0")
        print("   • If nums[n-1] < 0: all numbers negative → impossible to sum to 0")
        print()
        print("3. **Main Algorithm Loop**:")
        print("   • For i from 0 to n-3:")
        print("     - Skip duplicates: if nums[i] == nums[i-1], continue")
        print("     - Early termination: if nums[i] > 0, break (no more valid triplets)")
        print("     - Set left = i+1, right = n-1")
        print()
        print("4. **Two-Pointer Search**:")
        print("   • While left < right:")
        print("     - Calculate sum = nums[i] + nums[left] + nums[right]")
        print("     - If sum < 0: need larger sum → left++")
        print("     - If sum > 0: need smaller sum → right--")
        print("     - If sum == 0: found triplet!")
        print("       * Add [nums[i], nums[left], nums[right]] to result")
        print("       * Skip duplicates for both pointers")
        print("       * Move both pointers: left++, right--")
        print()
        print("5. **Duplicate Handling Strategy**:")
        print("   • Outer loop: Skip duplicate starting elements")
        print("   • Inner loop: After finding a valid triplet, skip duplicate left/right values")
        print("   • This ensures all triplets in result are unique")
        print()
        print("Algorithm Visualization for [-1, 0, 1, 2, -1, -4]:")
        print("After sorting: [-4, -1, -1, 0, 1, 2]")
        print("```")
        print("i=0(-4): left=1(-1), right=5(2) → sum=-3 < 0 → left++")
        print("i=0(-4): left=2(-1), right=5(2) → sum=-3 < 0 → left++")
        print("i=0(-4): left=3(0),  right=5(2) → sum=-2 < 0 → left++")
        print("i=0(-4): left=4(1),  right=5(2) → sum=-1 < 0 → left++")
        print("i=0(-4): left > right → done with i=0")
        print()
        print("i=1(-1): left=2(-1), right=5(2) → sum=0 ✓ → found [-1,-1,2]")
        print("i=2(-1): skip duplicate")
        print("i=3(0):  left=4(1),  right=5(2) → sum=3 > 0 → right--")
        print("i=3(0):  left=4(1),  right=4(1) → left=right → done")
        print("```")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity of the algorithm."""
        print("\nComplexity Analysis:")
        print()
        print("**Time Complexity: O(n²)**")
        print("Detailed Time Complexity Derivation:")
        print("1. **Sorting**: O(n log n) using efficient sorting algorithm (Timsort in Python)")
        print("2. **Main algorithm**: O(n²)")
        print("   • Outer loop: iterate through n-2 elements → O(n)")
        print("   • Inner two-pointer search: for each i, left and right traverse at most n elements")
        print("   • Each element is visited at most once by left pointer and once by right pointer")
        print("   • Total inner operations: O(n) for each of the O(n) outer iterations")
        print("3. **Overall**: O(n log n) + O(n²) = O(n²) (dominated by the quadratic term)")
        print()
        print("**Best vs Worst Case Analysis:**")
        print("• Best case: O(n²) - when early termination kicks in frequently")
        print("• Average case: O(n²) - typical performance")
        print("• Worst case: O(n²) - when no early termination is possible")
        print()
        print("**Space Complexity: O(1) auxiliary, O(k) for output**")
        print("Space Complexity Derivation:")
        print("1. **Auxiliary space**: O(1)")
        print("   • Only constant extra variables: i, left, right, current_sum, n")
        print("   • No additional data structures that grow with input size")
        print("   • In-place sorting doesn't count toward auxiliary space complexity")
        print()
        print("2. **Output space**: O(k) where k is the number of unique triplets")
        print("   • In worst case: k can be O(n²) when there are many valid triplets")
        print("   • Example: array with many zeros → multiple [0,0,0] type solutions")
        print("   • This is unavoidable as we must return all valid triplets")
        print()
        print("**Optimization Impact:**")
        print("• Early termination optimizations reduce practical runtime significantly")
        print("• Asymptotic complexity remains O(n²), but constants are much better")
        print("• Duplicate skipping reduces the number of operations in practice")
        print()
        print("**Comparison with Alternative Approaches:**")
        print("• Brute force (3 nested loops): O(n³) time, O(1) space")
        print("• Hash-based approach: O(n²) time, O(n) space")
        print("• Our optimized two-pointer: O(n²) time, O(1) space ← Best balance!")
        print()
        print("The two-pointer approach achieves optimal time complexity while maintaining")
        print("minimal space usage, making it the preferred solution for this problem.")

    @staticmethod
    def print_code() -> None:
        """Prints the code of the solution."""
        print("\nOptimized Solution with Type Checking (Educational Version):")
        print("    class Solution:")
        print("        def three_sum(self, nums: list[int]) -> list[list[int]]:")
        print("            # === TYPE CHECKING SECTION - REMOVE FOR LEETCODE SUBMISSION ===")
        print("            if not isinstance(nums, list):")
        print("                raise TypeError('nums must be a list')")
        print("            if not all(isinstance(num, int) for num in nums):")
        print("                raise TypeError('All elements in nums must be integers')")
        print("            # === END TYPE CHECKING SECTION ===")
        print("            ")
        print("            # Early termination for edge cases")
        print("            if len(nums) < 3:")
        print("                return []")
        print("            ")
        print("            nums.sort()")
        print("            result = []")
        print("            n = len(nums)")
        print("            ")
        print("            # Optimization: early exit if no valid triplets possible")
        print("            if nums[0] > 0 or nums[n-1] < 0:")
        print("                return []")
        print("            ")
        print("            for i in range(n - 2):")
        print("                if i > 0 and nums[i] == nums[i - 1]:")
        print("                    continue")
        print("                if nums[i] > 0:")
        print("                    break")
        print("                ")
        print("                left, right = i + 1, n - 1")
        print("                while left < right:")
        print("                    current_sum = nums[i] + nums[left] + nums[right]")
        print("                    if current_sum < 0:")
        print("                        left += 1")
        print("                    elif current_sum > 0:")
        print("                        right -= 1")
        print("                    else:")
        print("                        result.append([nums[i], nums[left], nums[right]])")
        print("                        while left < right and nums[left] == nums[left + 1]:")
        print("                            left += 1")
        print("                        while left < right and nums[right] == nums[right - 1]:")
        print("                            right -= 1")
        print("                        left += 1")
        print("                        right -= 1")
        print("            return result")
        print()
        print("LeetCode Submission Version (Type Checking Removed):")
        print("    class Solution:")
        print("        def threeSum(self, nums: List[int]) -> List[List[int]]:")
        print("            if len(nums) < 3:")
        print("                return []")
        print("            nums.sort()")
        print("            result = []")
        print("            n = len(nums)")
        print("            if nums[0] > 0 or nums[n-1] < 0:")
        print("                return []")
        print("            for i in range(n - 2):")
        print("                if i > 0 and nums[i] == nums[i - 1]:")
        print("                    continue")
        print("                if nums[i] > 0:")
        print("                    break")
        print("                left, right = i + 1, n - 1")
        print("                while left < right:")
        print("                    current_sum = nums[i] + nums[left] + nums[right]")
        print("                    if current_sum < 0:")
        print("                        left += 1")
        print("                    elif current_sum > 0:")
        print("                        right -= 1")
        print("                    else:")
        print("                        result.append([nums[i], nums[left], nums[right]])")
        print("                        while left < right and nums[left] == nums[left + 1]:")
        print("                            left += 1")
        print("                        while left < right and nums[right] == nums[right - 1]:")
        print("                            right -= 1")
        print("                        left += 1")
        print("                        right -= 1")
        print("            return result")
        print()
        print("Key Optimizations:")
        print("• Early termination when nums[i] > 0 (no more valid triplets possible)")
        print("• Early exit if smallest > 0 or largest < 0")
        print("• Improved edge case handling for arrays with < 3 elements")
        print("• Clear type checking section that can be easily removed")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for using the 3Sum Finder Program!")
        print("\nGoodbye!\n")

def main() -> None:
    """Main function to run the 3Sum Finder Program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        nums = IO.prompt_user_for_numbers()
        start_time = time.perf_counter()
        
        solution = Solution()
        triplets = solution.three_sum(nums)
        
        end_time = time.perf_counter()
        
        IO.print_triplets(triplets)
        IO.print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        IO.print_solution_title()
        IO.print_intuition()
        IO.print_approach()
        IO.print_complexity()
        IO.print_code()
        
    except ValueError as e:
        print(f"Error: {e}")
    
    finally:
        IO.print_thank_you_message()

if __name__ == "__main__":
    main()

# This code implements a solution to the 3Sum problem using a two-pointer approach.
# The program prompts the user for a list of integers, finds all unique triplets that sum
# to zero, and prints the results along with the runtime of the algorithm.
# The solution has a time complexity of O(n^2) and a space complexity of O(1) auxiliary space.