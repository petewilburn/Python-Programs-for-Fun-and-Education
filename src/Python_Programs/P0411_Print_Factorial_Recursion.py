#Python Program to find the factorial of a number using recursion
def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n-1)

def prompt_user():
    count = 0
    while count < 3:
        try:
            value = int(input("Enter an integer to find its factorial (0-999): "))
            if 0 <= value <= 999:
                return value
            else:
                count += 1
                print("Please enter a number between 0 and 999.")
        except ValueError:
            count += 1
            print(f"Invalid input. Please enter a valid integer.")
    if count == 3:
        return None

def print_factorial(num, factorial_result):
    print(f"The factorial of {num} is: {factorial_result}")

def main():
    num = prompt_user()
    if num is not None:
        factorial = calc_factorial(num)
        print_factorial(num, factorial)
    else:
        print("Too many invalid attempts. Exiting the program. \n\n *** goodbye! ***")
        return
    print("\n\n End of program. \n\n   ***   goodbye!   ***   \n\n")

if __name__ == "__main__":
    main()

# This code defines a function to calculate the factorial of a number
# using recursion. The main function prompts the user for input and displays the result.