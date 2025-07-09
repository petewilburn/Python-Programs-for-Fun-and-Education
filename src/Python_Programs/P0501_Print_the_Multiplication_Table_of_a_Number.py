#Python program to print a multiplication table for a given number

def print_multiplication_table(number: int) -> None:
    """Print the multiplication table for the given number."""
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i} \n")

def prompt_for_number() -> int | None:
    """Prompt the user for a number and return it."""
    count = 0
    while count < 3:
        try:
            number = int(input("Please enter a positive integer: "))
            if number <= 0:
                raise ValueError("The number must be positive.")
            return number
        except ValueError as e:
            print(f"Invalid input: {e}")
            count += 1
    print("Too many invalid attempts. Exiting.")
    print("\n\n   *** Goodbye! ***\n\n")
    return None

def main():
    """Main function to run the program."""
    print("This program prints the multiplication table for a given number.")
    number = prompt_for_number()
    if number is not None:
        print_multiplication_table(number)

if __name__ == "__main__":
    main()