# A Python program to solve the Container With Most Water problem.

# Minimum Python Version: 3.9

# -------------------------------------------------------------------------------------------------------
# File: P3011_Container_With_Most_Water.py
# Description: A Python program to find the maximum area of water that can be contained by two lines.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# -------------------------------------------------------------------------------------------------------

import time

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Finds the maximum area of water that can be contained by two lines.
        This function uses a two-pointer approach to achieve O(n) time complexity.
        :param height: List of heights of the lines.
        :return: Maximum area of water that can be contained.
        """
        if not isinstance(height, list):                          # Check if the input is a list. Type checking is for external function calling to ensure type safety.
            raise TypeError("Input must be a list of integers.")

        if not height or len(height) < 2:                         # If the list is empty or has less than two heights, return 0
            return 0

        left, right = 0, len(height) - 1                          # Initialize two pointers, one at the start and one at the end of the height list
        max_area = 0                                              # Initialize the maximum area to 0

        while left < right:                                       # While the two pointers do not meet
            if height[left] < height[right]:                      # If the height at the left pointer is less than the height at the right pointer
                area = height[left] * (right - left)              # Calculate the area formed by the left pointer and the right pointer. (width = right - left)
                left += 1                                         # Move the left pointer to the right
            else:                                                 # If the height at the right pointer is less than or equal to the height at the left pointer
                area = height[right] * (right - left)             # Calculate the area formed by the right pointer and the left pointer
                right -= 1                                        # Move the right pointer to the left

            if area > max_area:                                   # If the calculated area is greater than the current maximum area
                max_area = area                                   # Update the maximum area

        return max_area

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Container With Most Water Program!")
        print("\nThis program will find the maximum area of water that can be contained by two lines.")
        print("You will be prompted to enter the heights of the lines.")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the problem."""
        print("\nIntroduction:")
        print("The Container With Most Water is a classic algorithmic problem that demonstrates")
        print("the power of the two-pointer technique. Imagine you have a series of vertical")
        print("lines of different heights arranged on a coordinate plane.")
        print("\nVisualization:")
        print("  |     |           |")
        print("  |  |  |     |     |")
        print("  |  |  |  |  |  |  |")
        print("  +--+--+--+--+--+--+")
        print("  0  1  2  3  4  5  6")
        print("\nThe challenge is to select two lines that, together with the x-axis,")
        print("form a container capable of holding the maximum amount of water.")
        print("This problem teaches optimal decision-making and greedy algorithms.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement."""
        print("\nProblem Statement:")
        print("Given an integer array 'height' of length n, where height[i] represents")
        print("the height of the i-th vertical line drawn at position i on the x-axis.")
        print("\nObjective: Find two lines that together with the x-axis form a container")
        print("that can hold the maximum amount of water.")
        print("\nConstraints:")
        print("- The container cannot be slanted (water would spill)")
        print("- Water level is limited by the shorter of the two lines")
        print("- Area = width × height = (right_index - left_index) × min(height[left], height[right])")
        print("\nExample: height = [1,8,6,2,5,4,8,3,7]")
        print("Best container: between indices 1 and 8 (heights 8 and 7)")
        print("Area = (8-1) × min(8,7) = 7 × 7 = 49")
        print("\nGoal: Return the maximum area of water the container can store.")
        print("\nLet's get started!\n")

    @staticmethod
    def prompt_user_for_heights() -> list[int]:
        """Prompts the user to enter heights of lines and returns them as a list."""
        count = 0
        while count < 3:
            count += 1
            user_input = input("Enter heights of lines separated by spaces: ")
            try:
                heights = list(map(int, user_input.split()))
                if len(heights) < 2:
                    print("Please enter at least two heights.")
                    continue
                return heights
            except ValueError:
                print("Invalid input. Please enter integers only.")
        raise ValueError("Too many invalid attempts. Exiting the program.")
    
    @staticmethod
    def print_max_area(max_area: int) -> None:
        """Prints the maximum area of water that can be contained."""
        print(f"\nThe maximum area of water that can be contained is: {max_area}")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the program in milliseconds."""
        print(f"\nRuntime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Container With Most Water using Two-Pointer Approach")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the algorithm."""
        print("\nIntuition:")
        print("Think of this as finding the largest container formed by two vertical lines.")
        print("The area is determined by: Area = width × height")
        print("- Width = distance between two lines")
        print("- Height = shorter of the two lines (water spills over the shorter one)")
        print("\nKey insight: Start with maximum possible width (endpoints)")
        print("Then strategically move inward to potentially find greater heights.")
        print("Why move the shorter line? Moving the taller line can ONLY decrease area,")
        print("but moving the shorter line might find a taller line and increase area.")
    
    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the algorithm."""
        print("\nApproach:")
        print("1. Initialize two pointers: left = 0, right = n-1 (maximum width)")
        print("2. Calculate current area = min(height[left], height[right]) × (right - left)")
        print("3. Update max_area if current area is larger")
        print("4. Move the pointer with the shorter height inward:")
        print("   - If height[left] < height[right]: move left pointer right (left++)")
        print("   - Otherwise: move right pointer left (right--)")
        print("5. Repeat steps 2-4 until pointers meet")
        print("6. Return the maximum area found")
        print("\nWhy this works:")
        print("- We start with maximum width and gradually trade width for potentially better height")
        print("- Moving the shorter line is optimal because moving the taller line guarantees no improvement")
        print("- This ensures we explore all potentially better solutions without missing any")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity of the algorithm."""
        print("\nComplexity:")
        print("Time Complexity: O(n), where n is the number of lines.")
        print("\nTime Complexity Derivation:")
        print("1. We use two pointers starting at opposite ends of the array")
        print("2. In each iteration, we move exactly one pointer inward")
        print("3. Each element is visited at most once by each pointer")
        print("4. Total iterations = n-1 (when pointers meet)")
        print("5. Each iteration does constant work: O(1)")
        print("6. Therefore: O(n) × O(1) = O(n)")
        print("\nWhy moving the shorter line pointer is optimal:")
        print("- Moving the taller line pointer can only decrease or maintain area")
        print("- Moving the shorter line pointer might increase area (if we find a taller line)")
        print("- This ensures we don't miss any potentially larger areas")
        print("\nSpace Complexity: O(1)")
        print("\nSpace Complexity Derivation:")
        print("- Only using a constant number of variables: left, right, max_area, width, etc.")
        print("- No additional data structures that grow with input size")
        print("- Memory usage is independent of input size n")

    @staticmethod
    def print_code() -> None:
        """Prints the code of the solution."""
        print("\nCode:")
        print("class Solution:")
        print("    def maxArea(self, height: list[int]) -> int:")
        print("        if not isinstance(height, list):")
        print("            raise TypeError('Input must be a list of integers.')")
        print("        if not height or len(height) < 2:")
        print("            return 0")
        print("        left, right = 0, len(height) - 1")
        print("        max_area = 0")
        print("        while left < right:")
        print("            if height[left] < height[right]:")
        print("                area = height[left] * (right - left)")
        print("                left += 1")
        print("            else:")
        print("                area = height[right] * (right - left)")
        print("                right -= 1")
        print("            if area > max_area:")
        print("                max_area = area")
        print("        return max_area")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for using the Container With Most Water Program!")
        print("\nGoodbye!\n")

def main():
    """Main function to run the program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    try:
        heights = IO.prompt_user_for_heights()
        start_time = time.perf_counter()
        solution = Solution()
        max_area = solution.maxArea(heights)
        end_time = time.perf_counter()
        IO.print_max_area(max_area)
        IO.print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        IO.print_solution_title()
        IO.print_intuition()
        IO.print_approach()
        IO.print_complexity()
        IO.print_code()
    except ValueError as e:
        print(f"\nError: {e}")
    finally:
        IO.print_thank_you_message()

if __name__ == "__main__":
    main()  # Run the main function

# This code implements a solution to the Container With Most Water problem using a two-pointer approach.
# The program prompts the user for heights of lines, calculates the maximum area of water that can be contained,
# and prints the result along with the runtime of the algorithm.