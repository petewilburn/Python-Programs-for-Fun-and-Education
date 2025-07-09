#A Python program to check if a number is prime - Brute Force Method

def is_prime(number: int) -> bool:
    """Check if the number is prime."""
    if number <= 1:                                 # All prime numbers are greater than 1
        return False
    for i in range(2, int(number**0.5) + 1):        # Check divisibility from 2 to the square root of the number
        if number % i == 0:                         # A number cannot be divisible by a number greater than its square root
            return False                            # If the number is divisible by any number other than 1 and itself, it is not prime
    return True                                     # If no divisors were found, the number is prime

def prompt_for_input() -> int | None:
    """Prompt the user for a number and return it."""
    number = None
    count = 0
    while number is None and count < 3:
        count += 1
        try:
            number = int(input("Please enter a positive integer: "))
            if number < 0:
                raise ValueError("The number must be positive.")
            elif number == 0:
                raise ValueError("The number cannot be zero.")
            elif number == 1:
                raise ValueError("1 is not a prime number.")    
            return number
        except ValueError as e:
            print(f"Invalid input: {e}")
            number = None
    return None

def print_result(number: int, is_prime: bool) -> None:
    """Print the result based on whether the number is prime."""
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

def main():
    """Main function to run the program."""
    print("This program checks if a number is prime.")
    number = prompt_for_input()
    if number is None:
        print("Failed to enter a valid number after 3 attempts. Exiting the program. \n\n *** goodbye! ***")
        return
    is_prime_result = is_prime(number)
    print_result(number, is_prime_result)

if __name__ == "__main__":
    main()