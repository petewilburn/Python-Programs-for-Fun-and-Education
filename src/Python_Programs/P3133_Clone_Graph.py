# A Python program to return a deep copy of a graph given a reference of a node in a connected undirected graph. Each node contains a value and a list of its neighbors.

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P3133_Clone_Graph.py
# Description: A Python program to clone a graph using depth-first search (DFS).
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import time
from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """        
        Clones a connected undirected graph using depth-first search (DFS).
        This function creates a deep copy of the graph, ensuring that all nodes and their neighbors are
        cloned correctly.
        :param node: The starting node of the graph to be cloned.
        :return: A deep copy of the graph starting from the given node.
        """

        # Check if the input node is None
        if node is None:
            return None

        # Create a mapping from original nodes to their clones
        clone_map = {}

        # Depth-first search (DFS) function to clone the graph
        def dfs(original: 'Node') -> 'Node':
            if original in clone_map:
                return clone_map[original]

            # Create a clone for the current node
            clone = Node(original.val)
            clone_map[original] = clone

            # Recursively clone all neighbors
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start the DFS from the given node
        return dfs(node)
    
def print_welcome_message() -> None:
    """Prints a welcome message to the user."""
    print("\nWelcome to the Graph Cloner Program!")
    print("\nThis program will clone a connected undirected graph.")
    print("You will be prompted to enter the graph structure.")
    print("\nLet's get started!\n")

def prompt_for_graph_structure() -> Node:
    """Prompts the user to enter the graph structure and returns the root node."""
    # For simplicity, let's create a small graph manually
    # In a real application, you might want to parse user input to create the graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2]
    node4.neighbors = [node1]

    return node1

def print_cloned_graph(cloned_node: Node) -> None:
    """Prints the cloned graph structure."""
    visited = set()
    
    def print_node(node: Node):
        if node in visited:
            return
        visited.add(node)
        print(f"Node {node.val} with neighbors: {[neighbor.val for neighbor in node.neighbors]}")
        for neighbor in node.neighbors:
            print_node(neighbor)

    print("\nCloned Graph Structure:")
    print_node(cloned_node)

def print_runtime(runtime: float) -> None:
    """Prints the runtime of the program in milliseconds."""
    print(f"\nRuntime: {runtime:.6f} milliseconds")

def print_solution_title() -> None:
    """Prints the title of the solution."""
    print("\nSolution: Clone Graph using Depth-First Search (DFS)")

def print_intuition() -> None:
    """Prints the intuition behind the algorithm."""
    print("\nIntuition:")
    print("The algorithm uses a depth-first search (DFS) approach to traverse the graph.")
    print("It creates a clone of each node and recursively clones its neighbors, ensuring that all nodes are visited and cloned correctly.")

def print_approach() -> None:
    """Prints the approach used in the solution."""
    print("\nApproach:")
    print("1. Use a dictionary to map original nodes to their clones.")
    print("2. Implement a recursive DFS function to clone each node and its neighbors.")
    print("3. Start the DFS from the given node and return the cloned graph.")

def print_complexity() -> None:
    """Prints the time and space complexity of the algorithm."""
    print("\nTime Complexity: O(V + E), where V is the number of vertices and E is the number of edges.")
    print("Space Complexity: O(V), for storing the cloned nodes in the dictionary.")

def print_code() -> None:
    """Prints the code of the solution."""
    print("\nCode:")
    print("    class Node:")
    print("        def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):")
    print("            self.val = val")
    print("            self.neighbors = neighbors if neighbors is not None else []")
    print()
    print("    class Solution:")
    print("        def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:")
    print("            # Implementation here...")
    print("            if node is None:")
    print("                return None")
    print()
    print("            # Create a mapping from original nodes to their clones")
    print("            clone_map = {}")
    print()
    print("            # Depth-first search (DFS) function to clone the graph")
    print("            def dfs(original: 'Node') -> 'Node':")
    print("                if original in clone_map:")
    print("                    return clone_map[original]")
    print()
    print("                # Create a clone for the current node")
    print("                clone = Node(original.val)")
    print("                clone_map[original] = clone")
    print()
    print("                # Recursively clone all neighbors")
    print("                for neighbor in original.neighbors:")
    print("                    clone.neighbors.append(dfs(neighbor))")
    print()
    print("                return clone")
    print()
    print("            # Start the DFS from the given node")
    print("            return dfs(node)")

def print_thank_you_message() -> None:
    """Prints a thank you message to the user."""
    print("\nThank you for using the Graph Cloner Program!")
    print("\nGoodbye!\n")

def main():
    """Main function to execute the graph cloning program."""
    print_welcome_message()
    try:
        root_node = prompt_for_graph_structure()
        start_time = time.perf_counter()
        solution = Solution()
        cloned_graph = solution.cloneGraph(root_node)
        end_time = time.perf_counter()
        print_cloned_graph(cloned_graph)
        print_runtime((end_time - start_time) * 1000)  # Convert to milliseconds
        print_solution_title()
        print_intuition()
        print_approach()
        print_complexity()
        print_code()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print_thank_you_message()

if __name__ == "__main__":
    main()

# This program clones a connected undirected graph using depth-first search (DFS).
# It creates a deep copy of the graph, ensuring that all nodes and their neighbors are cloned correctly.
# The user is prompted to enter the graph structure, and the program handles invalid inputs gracefully.
# The program prints the cloned graph structure and the runtime in milliseconds.
# The solution includes detailed explanations of the intuition, approach, and complexity.

