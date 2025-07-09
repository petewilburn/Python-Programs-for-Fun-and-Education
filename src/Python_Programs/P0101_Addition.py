# Addition
# This program performs addition of two numbers provided by the user.
# Addition

def add_numbers(a, b) -> float:
    """Returns the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a + b

def print_welcome_message():
    print("Welcome to the Addition Program!")
    print("This program will add two numbers that you provide.")

def prompt_user_for_numbers() -> tuple:
    """Prompts the user for two numbers and returns them as a tuple."""
    count = 0
    while count < 3:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            count += 1
    raise ValueError("Too many invalid attempts. Exiting. \n\n   *** Goodbye! ***")

def print_result(num1, num2, result):
    """Prints the result of the addition."""
    print(f"The sum of {num1} and {num2} is: {result}")

def main():
    """Main function to execute the addition program."""
    try:
        num1, num2 = prompt_user_for_numbers()
        result = add_numbers(num1, num2)
        print_result(num1, num2, result)
    except ValueError as e:
        print(e)
