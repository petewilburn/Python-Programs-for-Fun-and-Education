# A Python program to solve the Linked List Cycle problem using Floyd's Cycle-Finding Algorithm.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3141_Linked_List_Cycle.py
# Description: A Python program to determine if a linked list has a cycle.
# Author: Peter W.
# License: MIT License
# Copyright (c) 2025 Peter W.
# ---------------------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Floyd's Cycle-Finding Algorithm implementation.
        
        Uses two pointers moving at different speeds to detect cycles in linked lists.
        This educational version includes type hints and detailed comments for learning.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the Linked List Cycle Detection Program! 🔗")
        print("This program uses Floyd's Cycle-Finding Algorithm (Tortoise and Hare)")
        print("to detect if a linked list contains a cycle.")
        print("\nLet's explore this fascinating algorithm!\n")

    @staticmethod
    def print_introduction() -> None:
        """Prints an introduction to the Linked List Cycle problem."""
        print("\nIntroduction:")
        print("The Linked List Cycle problem is a classic algorithmic challenge that demonstrates")
        print("the power of the two-pointer technique in detecting cycles in data structures.")
        print("\nReal-world applications:")
        print("- Detecting infinite loops in program execution")
        print("- Memory leak detection in garbage collection")
        print("- Cycle detection in dependency graphs")
        print("- Network routing loop prevention")
        print("- Database transaction deadlock detection")
        print("\nVisualization of a cycle:")
        print("```")
        print("    1 → 2 → 3 → 4")
        print("        ↑       ↓")
        print("        8 ← 7 ← 6 ← 5")
        print("```")
        print("In this example, node 8 points back to node 2, creating a cycle.")
        print("\nFloyd's algorithm uses two pointers moving at different speeds:")
        print("- Slow pointer (tortoise): moves 1 step at a time")
        print("- Fast pointer (hare): moves 2 steps at a time")
        print("If there's a cycle, the fast pointer will eventually catch up to the slow pointer!")

    @staticmethod
    def print_problem_statement() -> None:
        """Prints the problem statement for the Linked List Cycle problem."""
        print("\nProblem Statement:")
        print("Given the head of a linked list, determine if the linked list has a cycle in it.")
        print("\nDefinition:")
        print("A cycle exists if there is some node in the list that can be reached again")
        print("by continuously following the next pointer.")
        print("\nConstraints:")
        print("- The number of nodes in the list is in the range [0, 10^4]")
        print("- -10^5 ≤ Node.val ≤ 10^5")
        print("- pos is -1 or a valid index in the linked list")
        print("\nExamples:")
        print("1. List: [3,2,0,-4], pos = 1 (cycle connects to node index 1)")
        print("   Output: True")
        print("2. List: [1,2], pos = 0 (cycle connects to node index 0)")
        print("   Output: True")
        print("3. List: [1], pos = -1 (no cycle)")
        print("   Output: False")
        print("\nObjective: Return True if there is a cycle, False otherwise.")

    @staticmethod
    def prompt_for_input() -> ListNode:
        """Prompts the user to choose a test case and returns the corresponding linked list."""
        print("\nChoose a test case:")
        print("1. Linked list with cycle: [3,2,0,-4] with cycle at position 1")
        print("2. Linked list with cycle: [1,2] with cycle at position 0")
        print("3. Linked list without cycle: [1,2,3,4,5]")
        print("4. Empty list")
        print("5. Single node without cycle")
        print("6. Single node with self-cycle")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return IO.create_test_case(choice)
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid integer.")
    
    @staticmethod
    def create_test_case(choice: int) -> ListNode:
        """Creates a test case based on user choice."""
        if choice == 1:
            # [3,2,0,-4] with cycle at position 1
            head = ListNode(3)
            node2 = ListNode(2)
            node3 = ListNode(0)
            node4 = ListNode(-4)
            
            head.next = node2
            node2.next = node3
            node3.next = node4
            node4.next = node2  # Creates cycle back to node2
            
            print("Created: [3,2,0,-4] with cycle at position 1")
            return head
            
        elif choice == 2:
            # [1,2] with cycle at position 0
            head = ListNode(1)
            node2 = ListNode(2)
            
            head.next = node2
            node2.next = head  # Creates cycle back to head
            
            print("Created: [1,2] with cycle at position 0")
            return head
            
        elif choice == 3:
            # [1,2,3,4,5] without cycle
            head = ListNode(1)
            current = head
            for i in range(2, 6):
                current.next = ListNode(i)
                current = current.next
            
            print("Created: [1,2,3,4,5] without cycle")
            return head
            
        elif choice == 4:
            # Empty list
            print("Created: Empty list")
            return None
            
        elif choice == 5:
            # Single node without cycle
            head = ListNode(1)
            print("Created: [1] without cycle")
            return head
            
        elif choice == 6:
            # Single node with self-cycle
            head = ListNode(1)
            head.next = head  # Points to itself
            print("Created: [1] with self-cycle")
            return head
        
        return None
    
    @staticmethod
    def print_result(has_cycle: bool) -> None:
        """Prints the result of the cycle detection."""
        if has_cycle:
            print("\n✅ Result: CYCLE DETECTED!")
            print("The linked list contains a cycle.")
        else:
            print("\n❌ Result: NO CYCLE FOUND")
            print("The linked list does not contain a cycle.")

    @staticmethod
    def print_runtime(runtime: float) -> None:
        """Prints the runtime of the algorithm."""
        print(f"\n⏱️ Runtime: {runtime:.6f} milliseconds")

    @staticmethod
    def print_solution_title() -> None:
        """Prints the title of the solution."""
        print("\nSolution: Linked List Cycle Detection using Floyd's Cycle-Finding Algorithm")

    @staticmethod
    def print_intuition() -> None:
        """Prints the intuition behind Floyd's Cycle-Finding Algorithm."""
        print("\nIntuition (Floyd's Cycle-Finding Algorithm):")
        print("Think of this problem like a race track scenario:")
        print("\n🐢 Slow Runner (Tortoise): Moves 1 step at a time")
        print("🐰 Fast Runner (Hare): Moves 2 steps at a time")
        print("\nKey insights:")
        print("1. **If there's NO cycle**: The fast runner will reach the end first")
        print("2. **If there's a cycle**: The fast runner will eventually lap the slow runner")
        print("3. **Meeting point**: When they meet, we've detected a cycle!")
        print("\nVisualization of the chase:")
        print("```")
        print("Step 1: S   F       (S=slow, F=fast)")
        print("Step 2:  S    F")
        print("Step 3:   S     F")
        print("Step 4:    S  F     (F wraps around in cycle)")
        print("Step 5:     SF      (They meet! Cycle detected)")
        print("```")

    @staticmethod
    def print_approach() -> None:
        """Prints the approach used in Floyd's Cycle-Finding Algorithm."""
        print("\nApproach (Floyd's Cycle-Finding Algorithm):")
        print("1. **Initialize Two Pointers**: slow = head, fast = head")
        print("2. **Move at Different Speeds**: slow advances 1 step, fast advances 2 steps")
        print("3. **Loop Condition**: Continue while fast != null AND fast.next != null")
        print("4. **Cycle Detection**: If slow == fast, cycle detected → return True")
        print("5. **No Cycle**: If fast reaches end (null) → return False")
        print("\nImplementation details:")
        print("• Both pointers start at head for simplicity")
        print("• Check 'fast and fast.next' to avoid null pointer exceptions")
        print("• Meeting in cycle is guaranteed due to speed difference")
        print("• Algorithm terminates in O(n) time with O(1) space")

    @staticmethod
    def print_code() -> None:
        """Prints the implementation of Floyd's Algorithm."""
        print("\nFloyd's Cycle-Finding Algorithm Implementation:")
        print("```python")
        print("def hasCycle(self, head: ListNode) -> bool:")
        print("    # Initialize both pointers to head")
        print("    slow = head")
        print("    fast = head")
        print("    ")
        print("    # Move pointers until fast reaches end or they meet")
        print("    while fast and fast.next:")
        print("        slow = slow.next        # Move slow pointer 1 step")
        print("        fast = fast.next.next   # Move fast pointer 2 steps")
        print("        ")
        print("        if slow == fast:        # Pointers meet = cycle detected")
        print("            return True")
        print("    ")
        print("    return False               # Fast reached end = no cycle")
        print("```")
        print("\nKey Implementation Details:")
        print("• Both pointers start at head (not slow at head, fast at head.next)")
        print("• Check 'fast and fast.next' to avoid null pointer exceptions")
        print("• Fast pointer advances 2 steps, slow pointer advances 1 step")
        print("• If pointers meet (slow == fast), cycle is detected")
        print("• If fast reaches end (null), no cycle exists")

    @staticmethod
    def print_complexity() -> None:
        """Prints the time and space complexity analysis."""
        print("\nComplexity Analysis:")
        print("Time Complexity: O(n), where:")
        print("- n = number of nodes in the linked list")
        print("\nTime Complexity Derivation:")
        print("1. **No Cycle Case**: Fast pointer traverses at most n/2 nodes → O(n)")
        print("2. **Cycle Case**: Both pointers enter cycle within n steps → O(n)")
        print("3. **Meeting in Cycle**: Fast pointer gains 1 step per iteration")
        print("4. **Maximum Iterations**: At most cycle length C iterations to meet")
        print("5. **Total**: O(n + C) = O(n) since C ≤ n")
        print("\nMathematical Proof:")
        print("- When pointers meet: distance(slow) × 2 = distance(fast)")
        print("- In cycle: 2d - d = kC (where k = number of fast pointer cycles)")
        print("- Therefore: d = kC, meaning they meet after k complete cycles")
        print("- Since k ≤ n/C, total time remains O(n)")
        print("\nSpace Complexity: O(1)")
        print("\nSpace Complexity Breakdown:")
        print("- Two pointer variables: O(1) space")
        print("- No additional data structures needed")
        print("- No recursive call stack (iterative solution)")
        print("- Constant space regardless of input size")
        print("\nComparison with alternatives:")
        print("- Hash Set approach: O(n) time, O(n) space - uses extra memory")
        print("- Floyd's algorithm: O(n) time, O(1) space - optimal solution")
        print("- Brute force: O(n²) time - checking every possible cycle start")

    @staticmethod
    def print_edge_cases() -> None:
        """Prints edge cases and their handling."""
        print("\nEdge Cases Analysis:")
        print("1. **Empty List (head = null)**")
        print("   - while loop condition: fast = null, fast.next = error")
        print("   - Our check: 'fast and fast.next' prevents null pointer exception")
        print("   - Result: False (no cycle)")
        print("\n2. **Single Node, No Cycle**")
        print("   - fast = head, fast.next = null")
        print("   - while loop doesn't execute")
        print("   - Result: False (no cycle)")
        print("\n3. **Single Node, Self-Cycle**")
        print("   - fast = head, fast.next = head")
        print("   - First iteration: slow = head, fast = head")
        print("   - slow == fast → True (cycle detected)")
        print("\n4. **Two Nodes, Cycle**")
        print("   - Node1 → Node2 → Node1")
        print("   - Both pointers start at Node1")
        print("   - After 1 iteration: slow at Node2, fast at Node2")
        print("   - slow == fast → True (cycle detected)")
        print("\n5. **Large List, No Cycle**")
        print("   - Fast pointer reaches end in O(n/2) time")
        print("   - Efficient early termination")
        print("\n6. **Large List, Small Cycle**")
        print("   - Algorithm still O(n) regardless of cycle size")
        print("   - Space complexity remains O(1)")
        print("\nRobustness Features:")
        print("✅ Null pointer safety with 'fast and fast.next' check")
        print("✅ Works for all list sizes (0 to 10^4 nodes)")
        print("✅ Handles all possible cycle positions")
        print("✅ Memory efficient with constant space usage")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for exploring Floyd's Cycle-Finding Algorithm! 🎉")
        print("This elegant solution demonstrates the power of the two-pointer technique.")
        print("Remember: Sometimes the most efficient algorithms are also the most beautiful!")
        print("\nGoodbye! 👋\n")

def main():
    """Main function to run the Linked List Cycle program."""
    IO.print_welcome_message()
    IO.print_introduction()
    IO.print_problem_statement()
    
    try:
        head = IO.prompt_for_input()
        start_time = time.perf_counter()
        solution = Solution()
        has_cycle = solution.hasCycle(head)
        end_time = time.perf_counter()
        
        IO.print_result(has_cycle)
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

# This program demonstrates Floyd's Cycle-Finding Algorithm (Tortoise and Hare technique)
# for detecting cycles in linked lists with optimal time and space complexity.
# 
# Educational Features:
# - Comprehensive explanation of the two-pointer technique
# - Visual ASCII art demonstrations of cycle detection
# - Multiple test cases covering all edge cases
# - Detailed complexity analysis with mathematical proofs
# - Real-world applications and use cases
# - Interactive test case selection
# 
# Algorithm Highlights:
# - Time Complexity: O(n) - linear traversal
# - Space Complexity: O(1) - constant space usage
# - Optimal solution that beats hash-based approaches
# - Elegant mathematical foundation and proof
# 
# The program demonstrates one of the most beautiful algorithms in computer science,
# where a simple concept (two pointers at different speeds) solves a complex problem
# with optimal efficiency. This is a perfect example of algorithmic elegance!


