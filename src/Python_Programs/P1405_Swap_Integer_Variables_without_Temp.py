#Python program to swap two integer variables without using a third variable

def prompt_for_input() -> tuple[int, int] | None:
    """Prompt the user for two integers and return them."""
    try:
        a = int(input("Enter an integer value for a: "))
        b = int(input("Enter an integer value for b: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return None, None

def swap_variables(a: int, b: int) -> tuple[int, int]:
    """Swap two variables without using a third variable."""
    # Using tuple unpacking to swap values
    a, b = b, a
    return a, b

def print_result(a: int, b: int) -> None:
    """Print the values before and after swapping."""
    # Note: In the context of this function, 'a' and 'b' are already swapped
    print(f"Before Swap, Values: a = {b}, b = {a}")
    print(f"After Swap, Values: a = {a}, b = {b}")

def main():
    """Main function to execute the swap operation."""
    print("This program swaps two integer variables without using a third variable.")
    a, b = prompt_for_input()
    if a is not None and b is not None:
        a, b = swap_variables(a, b)
        print_result(a, b)

if __name__ == "__main__":
    main()

# This program has a function that swaps two variables without using a third variable.
# It prompts the user for input, performs the swap, and prints the results. 
# The swap is done using tuple unpacking in Python, which is a concise way to swap values.
# The program also handles invalid input gracefully by catching ValueError exceptions.



