# Python program to generate a random number between 1 and 100
import random

def generate_random_number():
    random.seed()  # Initialize the random number generator
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    return number

def print_random_number():
    random_number = generate_random_number()
    print(f"Random number generated: {random_number}")
# Main function to execute the random number generation
if __name__ == "__main__":
    print_random_number()
# This code generates a random integer between 1 and 100 and prints it.
# It uses the random module to ensure that the number is different each time the program is run