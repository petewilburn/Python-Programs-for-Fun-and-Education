#Python Program to find the factorial of a number using a for loop
def calc_factorial(num):
    if num != int(num):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def welcome_message():
    print("Welcome to the Factorial Calculator! \n"
          "  ***   Let's find the factorial of a number!   ***   " \
          "\n  \n      This program calculates the factorial of a number using a for loop. ")

def prompt_user():
    count = 0
    while count < 3:
        try:
            value = int(input("Enter an integer to find its factorial (0-42): "))
            if 0 <= value <= 42:
                return value
            else:
                count += 1
                print("Please enter a number between 0 and 42.")
        except ValueError:
            count += 1
            print("Invalid input. Please enter a valid integer. You have {} attempts left.".format(3 - count))
    if count == 3:
        return None

def print_factorial(num, factorial_result):
    print(f"The factorial of {num} is: {factorial_result}")

def main():
    welcome_message()
    num = prompt_user()
    if num is None:
        print("Too many invalid attempts. Exiting the program. \n\n *** goodbye! ***")
        return
    factorial = calc_factorial(num)
    print_factorial(num, factorial)

    print("\n\n End of program. \n\n   ***   goodbye!   ***   \n\n")

if __name__ == "__main__":
    main()

# This code defines a function to calculate the factorial of a number
# using recursion. The main function prompts the user for input and displays the result.