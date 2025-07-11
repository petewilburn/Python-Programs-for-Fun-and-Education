# A python program to display calendar for a given month and year

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P2001_Display_Calendar.py
# Description: A Python program to display the calendar for a given month and year.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import calendar

def display_calendar(year: int, month: int) -> None:
    try:
        calendar.setfirstweekday(calendar.SUNDAY)
        print("\n" + calendar.month(year, month))
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}. Please ensure the year is valid and the month is between 1 and 12.")

def print_welcome_message() -> None:
    print("\nWelcome to the Calendar Display Program!")
    print("This program will display the calendar for a given month and year.")
    print("You will be prompted to enter a year and a month.")
    print("\nLet's get started!\n")

def prompt_user_for_date() -> tuple[int, int]:
    count = 0
    while count < 3:
        try:
            year = int(input("Enter the year (e.g., 2023): "))
            month = int(input("Enter the month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            return year, month
        except ValueError as e:
            count += 1
            print(f"Invalid input: {e}. You have {3 - count} attempts left.\n")
    raise ValueError("Too many invalid attempts. Exiting the program.")

def main():
    print_welcome_message()
    try:
        year, month = prompt_user_for_date()
        display_calendar(year, month)
    except ValueError as e:
        print(e)
    finally:
        print("\nThank you for using the Calendar Display Program!")
        print("\nGoodbye!\n")

if __name__ == "__main__":
    main()

# This script prompts the user for a year and month, then displays the corresponding calendar.
# It includes error handling for invalid inputs.