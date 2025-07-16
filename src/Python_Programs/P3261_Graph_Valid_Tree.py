# A Python program to determine if a given graph is a valid tree.

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3261_Graph_Valid_Tree.py
# Description: A Python program to check if a given graph is a valid tree.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

"""
Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= a_i, b_i < n
- a_i != b_i
- There are no self-loops or repeated edges.
"""

import time

def validTree(n: int, edges: list[list[int]]) -> bool:
    """
    Checks if a given graph is a valid tree.
    
    :param n: Number of nodes in the graph
    :param edges: List of edges in the graph
    :return: True if the graph is a valid tree, False otherwise
    """

    # Validate the input parameters
    if not isinstance(n, int) or n < 0:
        raise ValueError("Number of nodes must be a non-negative integer.")
    if not isinstance(edges, list):
        raise ValueError("Edges must be a list of lists.")

    if n == 0:                             # An empty graph is considered a valid tree
        return True                        
    if len(edges) != n - 1:                # A valid tree must have exactly n-1 edges for n nodes
        return False

    parent = list(range(n))                # Initialize a parent array to represent each node's parent. Each node is its own parent initially.
    
    def find(x):                           # Finds the root of the node x
        if parent[x] != x:                 # If x is not its own parent
            parent[x] = find(parent[x])    # Path compression for efficiency
        return parent[x]                   # Return the root of the node

    for u, v in edges:                     # For each edge (u, v)
        pu, pv = find(u), find(v)          # Find the roots of u and v using the find function
        if pu == pv:                       # If both nodes have the same root, a cycle exists -> return False
            return False
        parent[pu] = pv                    # Union the two nodes by setting one node's parent to the other

    return True                            # If no cycles are found and the number of edges is n-1, return True indicating a valid tree

def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Graph Valid Tree Checker Program!")
    print("\nThis program will determine if a given graph is a valid tree.")
    print("You will be prompted to enter the number of nodes and edges.")
    print("\nLet's get started!\n")

def prompt_for_input_or_example() -> str:
    """
    Prompts the user to choose between entering their own input or using an example.
    
    :return: 'input' if the user wants to enter their own input, 'example' if they want to use an example
    """
    choice = input("Would you like to enter your own input or use an example? (input/example): ").strip().lower()
    if choice not in ['input', 'example']:
        print("Invalid choice. Please enter 'input' or 'example'.")
        return prompt_for_input_or_example()
    return choice

def generate_example_graph() -> tuple[int, list[list[int]]]:
    """
    Generates an example graph with 5 nodes and 4 edges.
    
    :return: A tuple containing the number of nodes and a list of edges
    """
    n = 5
    edges = [[0, 1], [1, 2], [1, 3], [2, 4]]
    return n, edges

def prompt_for_graph() -> tuple[int, list[list[int]]]:
    """
    Prompts the user for the number of nodes and edges in the graph.

    :return: A tuple containing the number of nodes and a list of edges
    """
    count = 0
    while count < 3:
        count += 1
        try:
            n = int(input("Enter the number of nodes in the graph: "))
            if n < 0:
                print("Number of nodes must be a non-negative integer.")
                continue
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number of nodes.")
    count = 0
    edges = []
    while count < 3:
        count += 1
        try:
            print(f"Enter {n-1} edges (format: u v) where u and v are node indices (0 to {n-1}):")
            u, v = map(int, input(f"Enter edge {count} (format: u v): ").split())
            if u < 0 or u >= n or v < 0 or v >= n:
                raise ValueError("Node indices must be between 0 and n-1.")
            if u == v:
                raise ValueError("An edge cannot connect a node to itself.")
            if [u, v] not in edges and [v, u] not in edges:
                edges.append([u, v])
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid edge.")
    return n, edges

def print_result(is_valid: bool) -> None:
    """Prints the result of the graph validity check."""
    if is_valid:
        print("\nThe graph is a valid tree.")
    else:
        print("\nThe graph is not a valid tree.")

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program in milliseconds."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_solution_title() -> None:
    """Prints the title of the solution."""
    print("\nSolution: Graph Valid Tree Check using Union-Find Approach")

def print_intuition() -> None:
    """Prints the intuition behind the algorithm."""
    print("\nIntuition:")
    print("A valid tree must have exactly n-1 edges for n nodes and must be connected without cycles.")
    print("We can use a Union-Find data structure to efficiently check for cycles and connectivity.")

def print_approach() -> None:
    """Prints the approach used in the solution."""
    print("\nApproach:")
    print("1. Initialize a parent array to represent each node's parent.")
    print("2. For each edge, find the roots of both nodes.")
    print("3. If both nodes have the same root, a cycle exists; return False.")
    print("4. Otherwise, union the two nodes by setting one node's parent to the other.")
    print("5. Finally, check if the number of edges is n-1.")

def print_complexity() -> None:
    """Prints the time and space complexity of the algorithm."""
    print("\nTime Complexity: O(E * α(V)), where E is the number of edges, V is the number of vertices, and α is the inverse Ackermann function.")
    print("Space Complexity: O(V), for storing the parent array.")

def print_code() -> None:
    """Prints the code of the solution."""
    print("\nCode:")
    print("    def validTree(n: int, edges: List[List[int]]) -> bool:")
    print("        if n == 0:")
    print("            return True")
    print("        if len(edges) != n - 1:")
    print("            return False")
    print("        parent = list(range(n))")
    print("        def find(x):")
    print("            if parent[x] != x:")
    print("                parent[x] = find(parent[x])")
    print("            return parent[x]")
    print("        for u, v in edges:")
    print("            pu, pv = find(u), find(v)")
    print("            if pu == pv:")
    print("                return False")
    print("            parent[pu] = pv")
    print("        return True")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Graph Valid Tree Checker Program!")
    print("\nGoodbye!\n")

def main():
    """Main function to run the program."""
    print_welcome_message()
    try:
        choice = prompt_for_input_or_example()
        if choice == 'example':
            n, edges = generate_example_graph()
        else:
            n, edges = prompt_for_graph()
        start_time = time.perf_counter()
        is_valid = validTree(n, edges)
        end_time = time.perf_counter()
        print_result(is_valid)
        print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        print_solution_title()
        print_intuition()
        print_approach()
        print_complexity()
        print_code()
    except ValueError as e:
        print(f"An error occurred: {e}")
    finally:
        print_thank_you_message()

if __name__ == "__main__":
    main()

# This code implements a solution to check if a given graph is a valid tree using the Union-Find approach.
# The program prompts the user for the number of nodes and edges, checks for cycles, and verifies connectivity.
# It handles invalid inputs gracefully and provides detailed output about the solution. 
# The program is designed to be user-friendly and robust against invalid inputs.
# The solution includes explanations of the intuition, approach, complexity, and the code itself.

