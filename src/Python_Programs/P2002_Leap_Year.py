#A Python program to check for a leap year

def prompt_for_input() -> int | None:
    """Prompt the user for a year and return it."""
    try:
        year = int(input("Please enter a year: "))
        if year <= 0:
            raise ValueError("The year cannot be negative or 0.")
        elif year > 9999:
            raise ValueError("Year must be a four-digit integer number.")
        return year
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return None

def check_leap_year(year: int) -> bool:
    """Check if the year is a leap year."""
    # A year is a leap year if it is divisible by 4,
    # except for end-of-century years, which must be divisible by 400.
    if not isinstance(year, int):
        raise ValueError("Input must be an integer.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def print_result(year: int, is_leap: bool) -> None:
    """Print the result based on whether the year is a leap year."""
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if not isinstance(is_leap, bool):
        raise ValueError("is_leap must be a boolean value.")
    if is_leap:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def main():
    """Main function to run the program."""
    print("This program checks if a year is a leap year.")
    year = None
    count = 0
    while year is None and count < 3:
        count += 1
        year = prompt_for_input()
    if year is not None:
        is_leap = check_leap_year(year)
        print_result(year, is_leap)
    else:
        print("Failed to enter a valid year after 3 attempts. Exiting the program. \n\n *** goodbye! ***")

if __name__ == "__main__":
    main()

# This program checks if a year is a leap year.
# It prompts the user for input and handles invalid entries gracefully.
# The user has three attempts to enter a valid year.
# The program then checks the year and prints whether it is a leap year or not.
# The program is designed to be user-friendly and robust against invalid inputs.
# It uses the rules of leap years to determine the result.