#Python program to print prime numbers in a given range

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start: int, end: int) -> list[int]:
    """Print all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def prompt_for_range() -> tuple[int, int]:
    """Prompt user for a range and print prime numbers in that range."""
    count = 0
    while count < 3:
        try:
            start = int(input("Enter the start of the range (greater than 1): "))
            end = int(input("Enter the end of the range (maximum 999): "))
            if start > end:
                print("Start of the range must be less than or equal to the end.")
                count += 1
                continue
            elif start < 2 or end > 999:
                print("Please ensure the start of the range is greater than 1 and the end of the range less than 1,000.")
                count += 1
                continue
            primes = find_primes_in_range(start, end)
            print(f"Prime numbers between {start} and {end}: {primes}")
        except ValueError:
            print("Please enter valid integers.")
    if count >= 3:
        print("Too many invalid attempts. Exiting the program.")
        return None, None
    return start, end

def print_primes_in_range(primes: list[int], start: int, end: int) -> None:
    """Print prime numbers in the specified range."""
    if primes:
        print(f"Prime numbers between {start} and {end}: {primes}")
    else:
        print(f"There are no prime numbers between {start} and {end}.")

def main() -> None:
    start, end = prompt_for_range()
    if start is not None and end is not None:
        primes = find_primes_in_range(start, end)
        print_primes_in_range(primes, start, end)

if __name__ == "__main__":
    main()

# This script finds and prints all prime numbers in a user-specified range.
# It includes error handling for invalid inputs and limits the range to 1-999.
