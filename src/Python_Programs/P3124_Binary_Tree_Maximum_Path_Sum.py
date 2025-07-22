# A Python program to solve the Binary Tree Maximum Path Sum problem using Depth-First Search.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3124_Binary_Tree_Maximum_Path_Sum.py
# Description: A Python program to find the maximum path sum in a binary tree.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Finds the maximum path sum in a binary tree using DFS with global tracking.
        
        This educational version includes comprehensive error handling and detailed comments.
        Uses depth-first search with a global maximum to track the best path sum.
        """
        if not root:
            return 0
        
        self.max_sum = float('-inf')
        
        def max_gain(node):
            """
            Returns the maximum gain from the current node to any leaf node.
            Updates the global maximum path sum during traversal.
            """
            if not node:
                return 0
            
            # Recursively get max gain from left and right subtrees
            # Use max(0, gain) to ignore negative paths
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))
            
            # Calculate the path sum passing through current node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum if current path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain from current node (can only use one path)
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Binary Tree Maximum Path Sum Program! 🌳")
        print("This program uses depth-first search to find the maximum sum path")
        print("in a binary tree, where a path can start and end at any nodes.")
        print("\nLet's explore this fascinating tree traversal algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Binary Tree Maximum Path Sum problem."""
        print("\nIntroduction:")
        print("The Binary Tree Maximum Path Sum problem is a classic tree traversal challenge")
        print("that demonstrates the power of depth-first search and dynamic programming.")
        print("\nReal-world applications:")
        print("- Network flow optimization and bottleneck analysis")
        print("- Financial portfolio path optimization")
        print("- Resource allocation in hierarchical systems")
        print("- Decision tree analysis and path evaluation")
        print("- Supply chain cost optimization")
        print("\nVisualization of maximum path sum:")
        print("```")
        print("     10")
        print("    /  \\")
        print("   2    10")
        print("  / \\     \\")
        print(" 20  1     -25")
        print("          /  \\")
        print("         3    4")
        print("```")
        print("Maximum path: 20 → 2 → 10 → 10 = 42")
        print("\nA path is defined as any sequence of nodes from some starting node")
        print("to any node in the tree along the parent-child connections.")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Binary Tree Maximum Path Sum problem."""
        print("\nProblem Statement:")
        print("Given the root of a binary tree, return the maximum path sum of any")
        print("non-empty path in the tree.")
        print("\nDefinition:")
        print("A path in a binary tree is a sequence of nodes where each pair of")
        print("adjacent nodes in the sequence has an edge connecting them.")
        print("A node can only appear in the sequence at most once.")
        print("\nConstraints:")
        print("- The number of nodes in the tree is in the range [1, 3 × 10^4]")
        print("- -1000 ≤ Node.val ≤ 1000")
        print("- A path does not need to pass through the root")
        print("- A path can start and end at any nodes in the tree")
        print("\nExamples:")
        print("1. Tree: [1,2,3] → Output: 6 (path: 2→1→3)")
        print("2. Tree: [-10,9,20,null,null,15,7] → Output: 42 (path: 15→20→7)")
        print("3. Tree: [-3] → Output: -3 (single node)")
        print("\nObjective: Return the maximum sum of any path in the tree.")

    @staticmethod
    def prompt_for_input() -> TreeNode:
        """Prompts the user to choose a test case and returns the corresponding binary tree."""
        print("\nChoose a test case:")
        print("1. Standard case: [1,2,3] (simple tree)")
        print("2. Complex case: [-10,9,20,null,null,15,7] (mixed values)")
        print("3. Negative values: [-3] (single negative node)")
        print("4. All negative: [-1,-2,-3] (all negative values)")
        print("5. Large positive: [5,4,8,11,null,13,4,7,2,null,null,null,1]")
        print("6. Zigzag path: [2,-1,-2]")
        print("7. Deep tree: [1,2,null,3,null,4,null]")
        
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
    def create_test_case(choice: int) -> TreeNode:
        """Creates a test case based on user choice."""
        if choice == 1:
            # Tree: [1,2,3]
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            print("Created tree: [1,2,3] - Expected max path sum: 6")
            return root
            
        elif choice == 2:
            # Tree: [-10,9,20,null,null,15,7]
            root = TreeNode(-10)
            root.left = TreeNode(9)
            root.right = TreeNode(20)
            root.right.left = TreeNode(15)
            root.right.right = TreeNode(7)
            print("Created tree: [-10,9,20,null,null,15,7] - Expected max path sum: 42")
            return root
            
        elif choice == 3:
            # Tree: [-3]
            root = TreeNode(-3)
            print("Created tree: [-3] - Expected max path sum: -3")
            return root
            
        elif choice == 4:
            # Tree: [-1,-2,-3]
            root = TreeNode(-1)
            root.left = TreeNode(-2)
            root.right = TreeNode(-3)
            print("Created tree: [-1,-2,-3] - Expected max path sum: -1")
            return root
            
        elif choice == 5:
            # Tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
            root = TreeNode(5)
            root.left = TreeNode(4)
            root.right = TreeNode(8)
            root.left.left = TreeNode(11)
            root.left.left.left = TreeNode(7)
            root.left.left.right = TreeNode(2)
            root.right.left = TreeNode(13)
            root.right.right = TreeNode(4)
            root.right.right.right = TreeNode(1)
            print("Created tree: [5,4,8,11,null,13,4,7,2,null,null,null,1] - Expected max path sum: 48")
            return root
            
        elif choice == 6:
            # Tree: [2,-1,-2]
            root = TreeNode(2)
            root.left = TreeNode(-1)
            root.right = TreeNode(-2)
            print("Created tree: [2,-1,-2] - Expected max path sum: 2")
            return root
            
        elif choice == 7:
            # Tree: [1,2,null,3,null,4,null] (deep tree)
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.left.left = TreeNode(3)
            root.left.left.left = TreeNode(4)
            print("Created tree: [1,2,null,3,null,4,null] - Expected max path sum: 10")
            return root
        
        return None
    
    @staticmethod
    def print_result(max_sum: int) -> None:
        """Prints the result of the maximum path sum calculation."""
        print(f"\n✅ Result: {max_sum}")
        print("Successfully found the maximum path sum in the binary tree!")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Binary Tree Maximum Path Sum using Depth-First Search")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind the Binary Tree Maximum Path Sum algorithm."""
        print("\nIntuition (DFS with Global Maximum Tracking):")
        print("Think of this problem as finding the best route through a tree network:")
        print("\n🌳 Tree Traversal: Visit each node and consider all possible paths")
        print("💰 Path Value: Sum of node values along any valid path")
        print("🎯 Global Maximum: Track the best path found so far")
        print("\nKey insights:")
        print("1. **Path Types**: A path can go through a node or start/end at it")
        print("2. **Local vs Global**: Each node can contribute to global max or return gain")
        print("3. **Negative Handling**: Ignore negative subtree contributions")
        print("4. **DFS Pattern**: Post-order traversal to get subtree information first")
        print("\nVisualization of path consideration:")
        print("```")
        print("     A")
        print("    / \\")
        print("   B   C")
        print("  /")
        print(" D")
        print("```")
        print("At node A: Consider paths B→A→C, D→B→A→C, A→C, A→B→D, etc.")
        print("Return to parent: max(A→B, A→C) + A.val for further path building")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in the Binary Tree Maximum Path Sum algorithm."""
        print("\nApproach (Post-order DFS with Global Maximum):")
        print("1. **DFS Traversal**: Use post-order to get subtree information first")
        print("2. **Max Gain Function**: Calculate maximum gain from current node downward")
        print("3. **Path Through Node**: Consider path that goes through current node")
        print("4. **Global Update**: Update global maximum with best path through current node")
        print("5. **Return Gain**: Return maximum gain for parent to use in its calculations")
        print("\nImplementation details:")
        print("• Use global variable to track maximum path sum across all nodes")
        print("• For each node, calculate max gain from left and right subtrees")
        print("• Ignore negative gains (use max(0, gain)) to avoid detrimental paths")
        print("• Update global max with path sum through current node")
        print("• Return the better single-direction gain for parent node")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of the Binary Tree Maximum Path Sum algorithm."""
        print("\nBinary Tree Maximum Path Sum Algorithm Implementation:")
        print("```python")
        print("def maxPathSum(self, root: TreeNode) -> int:")
        print("    if not root:")
        print("        return 0")
        print("    ")
        print("    self.max_sum = float('-inf')")
        print("    ")
        print("    def max_gain(node):")
        print("        if not node:")
        print("            return 0")
        print("        ")
        print("        # Get max gain from subtrees (ignore negative)")
        print("        left_gain = max(0, max_gain(node.left))")
        print("        right_gain = max(0, max_gain(node.right))")
        print("        ")
        print("        # Path sum through current node")
        print("        current_path_sum = node.val + left_gain + right_gain")
        print("        ")
        print("        # Update global maximum")
        print("        self.max_sum = max(self.max_sum, current_path_sum)")
        print("        ")
        print("        # Return max gain for parent")
        print("        return node.val + max(left_gain, right_gain)")
        print("    ")
        print("    max_gain(root)")
        print("    return self.max_sum")
        print("```")
        print("\nKey Implementation Details:")
        print("• Use post-order DFS to get subtree information before processing parent")
        print("• Global variable tracks maximum path sum found across all nodes")
        print("• max(0, gain) ignores negative subtree contributions")
        print("• Current path sum considers path going through the node (both subtrees)")
        print("• Return value considers only one subtree (for parent's path building)")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n), where:")
        print("- n = number of nodes in the binary tree")
        print("\nTime Complexity Derivation:")
        print("1. **DFS Traversal**: Visit each node exactly once → O(n)")
        print("2. **Per Node Work**: Constant time operations at each node → O(1)")
        print("3. **Global Updates**: Constant time maximum comparison → O(1)")
        print("4. **Subtree Calculations**: Each edge traversed twice (down and up) → O(n)")
        print("5. **Total**: O(n) - linear traversal of all nodes")
        print("\nMathematical Proof:")
        print("Let T(n) be the time to process a tree with n nodes")
        print("\n**Recurrence Relation:**")
        print("- T(n) = T(left_subtree) + T(right_subtree) + O(1)")
        print("- T(0) = O(1) (base case: null node)")
        print("\n**Proof by Induction:**")
        print("- Base case: T(1) = 2×T(0) + O(1) = O(1) ✓")
        print("- Inductive step: If T(k) = O(k) for all k < n")
        print("- Then T(n) = O(left_size) + O(right_size) + O(1) = O(n)")
        print("- Since left_size + right_size = n-1 < n")
        print("\n**Optimality Analysis:**")
        print("- Must visit each node to determine its contribution → Ω(n) lower bound")
        print("- Our algorithm visits each node exactly once → O(n) upper bound")
        print("- Therefore: T(n) = Θ(n) - optimal for this problem")
        print("\nSpace Complexity: O(h), where h = height of the tree")
        print("\nSpace Complexity Breakdown:")
        print("- Recursive call stack: O(h) space for DFS")
        print("- Global variables: O(1) space")
        print("- No additional data structures needed")
        print("- Best case (balanced tree): O(log n) space")
        print("- Worst case (skewed tree): O(n) space")
        print("\nComparison with alternatives:")
        print("- Brute force (all paths): O(n^3) time - exponential paths")
        print("- Dynamic programming: O(n) time, O(n) space - similar but more memory")
        print("- Our DFS approach: O(n) time, O(h) space - optimal solution")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Single Node Tree**")
        print("   - Input: [5] (single positive node)")
        print("   - Handling: Return the node value directly")
        print("   - Result: 5 (path consists of just the node)")
        print("\n2. **Single Negative Node**")
        print("   - Input: [-3] (single negative node)")
        print("   - Handling: Must include the node (path cannot be empty)")
        print("   - Result: -3 (forced to take the negative value)")
        print("\n3. **All Negative Values**")
        print("   - Input: [-1,-2,-3] (all nodes negative)")
        print("   - Handling: Choose the least negative single node")
        print("   - Result: -1 (avoid adding more negative values)")
        print("\n4. **Balanced Tree with Mixed Values**")
        print("   - Input: [10,-5,15,null,null,6,20]")
        print("   - Handling: Standard DFS with negative gain filtering")
        print("   - Result: 41 (path: 6→15→20 or similar)")
        print("\n5. **Deep Linear Tree**")
        print("   - Input: [1,2,null,3,null,4,null] (linked list structure)")
        print("   - Handling: DFS works but uses O(n) stack space")
        print("   - Result: 10 (path: 1→2→3→4)")
        print("\n6. **Wide Tree**")
        print("   - Input: Tree with many children at each level")
        print("   - Handling: DFS explores all subtrees efficiently")
        print("   - Result: Optimal path found through systematic exploration")
        print("\nRobustness Features:")
        print("✅ Handles trees of any shape (balanced, skewed, complete)")
        print("✅ Correctly processes negative values with max(0, gain)")
        print("✅ Efficiently tracks global maximum across all possible paths")
        print("✅ Uses optimal O(n) time and O(h) space complexity")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring the Binary Tree Maximum Path Sum Algorithm! 🎉")
        print("This solution demonstrates the power of depth-first search and")
        print("dynamic programming in solving complex tree traversal problems.")
        print("\nRemember: Tree algorithms often combine traversal with optimization!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Binary Tree Maximum Path Sum program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        root = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        max_sum = solution.maxPathSum(root)
        end_time = time.perf_counter()
        
        IO.print_result(max_sum)
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

# This program demonstrates depth-first search for solving the Binary Tree Maximum Path Sum
# problem with optimal time complexity and comprehensive edge case handling.
# 
# Educational Features:
# - Comprehensive explanation of DFS and dynamic programming concepts
# - Visual demonstrations of tree traversal and path consideration
# - Multiple test cases covering all edge cases and tree structures
# - Detailed complexity analysis with mathematical proofs
# - Real-world applications of tree optimization problems
# - Interactive test case selection with expected results
# 
# Algorithm Highlights:
# - Time Complexity: O(n) - visits each node exactly once
# - Space Complexity: O(h) - recursive stack depth
# - Handles negative values optimally with gain filtering
# - Uses post-order DFS for bottom-up optimization
# 
# The program demonstrates how tree traversal algorithms can elegantly solve
# optimization problems by combining local decisions with global tracking.
# Perfect for understanding dynamic programming on trees!
