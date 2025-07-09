#A Python program to check if an integer is odd or even

def prompt_for_input() -> int | None:
    """Prompt the user for an integer and return it."""
    try:
        number = int(input("Please enter an integer: "))
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def check_for_zero(number: int) -> bool:
    """Check if the number is zero."""
    if number == 0:
        print("The number is zero.")
        return True
    return False

def check_odd_even(number: int) -> str:
    """Check if the number is odd or even."""
    # Check if the number is even or odd using modulus operator
    numtype = "None"
    if number % 2 == 0:
        numtype = "Even"
    else:
        numtype = "Odd" 
    return numtype

def print_result(numtype: str) -> None:
    """Print the result based on the number type."""
    print(f"The number is: {numtype}")

def main():
    """Main function to run the program."""
    print("This program checks if an integer is odd or even.")
    number = None
    count = 0
    while number is None and count < 3:
        count += 1
        number = prompt_for_input()
    if number is not None:
        if check_for_zero(number):
            return
        numtype = check_odd_even(number)
        print_result(numtype)
    else:
        print("Failed to enter a valid integer after 3 attempts. Exiting the program. \n\n *** goodbye! ***")

if __name__ == "__main__":
    main()

# This program checks if an integer is odd or even.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid integer.
# The program then checks the integer and prints whether it is odd or even.
# The program is designed to be user-friendly and robust against invalid inputs.
# It uses a simple modulus operation to determine the odd/even status.
