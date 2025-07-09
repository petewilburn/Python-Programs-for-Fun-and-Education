# A Python Program to print all prime numbers in an interval
# using the Sieve of Eratosthenes algorithm

def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm."""
    primes = []
    is_prime = [True] * (n + 1)                             # Create a boolean array "is_prime[0..n]" and initialize all entries as true.
    is_prime[0] = is_prime[1] = False                       # 0 and 1 are not prime numbers

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:                                     # If is_prime[p] is still true, then it is a prime number
            for multiple in range(p * p, n + 1, p):         # Mark all multiples of p as not prime
                is_prime[multiple] = False                  
    primes = [p for p in range(2, n + 1) if is_prime[p]]    # Collect all primes after sieving
    return primes

def prompt_user_for_input():
    """Prompts the user for an upper limit and returns it."""
    for _ in range(3):
        try:
            number = int(input("Enter an upper limit (2 to 999,999) to find prime numbers: "))
            if 2 <= number < 1000000:
                return number
            else:
                print("The number must be between 2 and 999,999.")
        except ValueError:
            print("Please enter a valid integer.")
    return None

def print_primes(primes):
    """Prints the list of prime numbers, summarizing if the list is very long."""
    if not primes:
        print("No prime numbers found.")
        return
    max_display = 20
    if len(primes) <= max_display:
        print("Prime numbers:", ', '.join(map(str, primes)))
    else:
        print(f"Prime numbers (showing first {max_display//2} and last {max_display//2} of {len(primes)}):")
        print(', '.join(map(str, primes[:max_display//2])) + ', ... ' +
              ', '.join(map(str, primes[-max_display//2:])))

def main():
    """Main function to execute the Sieve of Eratosthenes and print prime numbers."""

    number = prompt_user_for_input()
    if number is None:
        print("Failed to enter a valid number after 3 attempts. Exiting the program. \n\n *** goodbye! ***")
        return
    primes = sieve_of_eratosthenes(number)
    print_primes(primes)

if __name__ == "__main__":
    main()


# This code will prompt the user for an upper limit and print all prime numbers up to that limit using the Sieve of Eratosthenes algorithm.
# The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a specified integer n.
# It works by iteratively marking the multiples of each prime number starting from 2.   
# The time complexity of this algorithm is O(n log log n), making it very efficient for large values of n.
# The space complexity is O(n) due to the storage of the boolean array. 
# The program handles edge cases by checking if the input is less than 2 and informs the user accordingly.
# The output is a list of prime numbers, which can be used for further processing or analysis.
# The program is designed to be user-friendly, providing clear instructions and output formatting.  

