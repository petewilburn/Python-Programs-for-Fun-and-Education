# A python program to display calendar for a given month and year
import calendar
def prompt_user_for_date() -> tuple[int, int]:
    try:
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if year < 1 or year > 9999:
            raise ValueError("Year must be between 1 and 9999.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return prompt_user_for_date()
    return year, month

def display_calendar(year: int, month: int) -> None:
    try:
        print(calendar.month(year, month))
    except calendar.IllegalMonthError:
        print("The month must be between 1 and 12.")
    except calendar.IllegalYearError:
        print("The year must be between 1 and 9999.")

def main():
    year, month = prompt_user_for_date()
    display_calendar(year, month)

if __name__ == "__main__":
    main()

# This script prompts the user for a year and month, then displays the corresponding calendar.
# It includes error handling for invalid inputs.