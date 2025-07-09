#A Python program to check if a number is positive, negative, or zero

def prompt_for_input() -> float | None:
    """Prompt the user for a number and return it."""
    try:
        number = float(input("Please enter a number: "))
        return number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def check_number(number: float) -> str:
    """Check if the number is positive, negative, or zero."""
    numtype = "None"
    if number > 0:
        numtype = "Positive"
    elif number < 0:
        numtype = "Negative"
    else:
        numtype = "Zero"
    return numtype

def print_result(numtype: str) -> None:
    """Print the result based on the number type."""
    print(f"The number is: {numtype}")

def main():
    """Main function to run the program."""
    print("This program checks if a number is positive, negative, or zero.")
    number = None
    count = 0
    while number is None and count < 3:
        count += 1
        number = prompt_for_input()
    if number is not None:
        numtype = check_number(number)
        print_result(numtype)
    else:
        print("Failed to enter a valid number after 3 attempts. Exiting the program. \n\n *** goodbye! ***")

if __name__ == "__main__":
    main()

# This program checks if a number is positive, negative, or zero.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid number.
# The program then checks the number and prints whether it is positive, negative, or zero.
# The program is designed to be user-friendly and robust against invalid inputs.
    