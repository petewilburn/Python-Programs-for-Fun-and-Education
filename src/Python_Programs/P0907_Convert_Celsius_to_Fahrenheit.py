# Python program to convert Celsius to Fahrenheit

# Minimum Python Version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P0907_Convert_Celsius_to_Fahrenheit.py
# Description: A Python program to convert temperatures between Celsius and Fahrenheit.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number (int or float).")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number (int or float).")
    return (fahrenheit - 32) * 5/9

def print_welcome_message() -> None:
    """
    Print a welcome message to the user.
    """
    print("\nWelcome to the Temperature Converter Program!")
    print("This program will convert temperatures between Celsius and Fahrenheit.")
    print("You will be prompted to enter a temperature and choose the conversion direction.")
    print("\nLet's get started!\n")

def prompt_conversion_choice() -> str | None:
    """
    Prompt the user to choose a conversion direction.
    
    :return: 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius
    """
    try:
        choice = input("Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").strip().upper()
        if choice not in ['C', 'F']:
            raise ValueError("Invalid choice. Please enter 'C' or 'F'.")
        return choice
    except ValueError as e:
        print(e)
        return prompt_conversion_choice()

def prompt_for_celsius() -> float | None:
    """
    Prompt the user for a temperature in Celsius.
    
    :return: Temperature in Celsius
    """
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        return celsius
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return prompt_for_celsius()

def prompt_for_fahrenheit() -> float | None:
    """
    Prompt the user for a temperature in Fahrenheit.
    
    :return: Temperature in Fahrenheit
    """
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        return fahrenheit
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return prompt_for_fahrenheit()

def main():
    """
    Main function to execute the Celsius to Fahrenheit or Fahrenheit to Celsius conversion.
    """
    print_welcome_message()
    try:
        choice = prompt_conversion_choice()
        if choice == 'C':
            celsius = prompt_for_celsius()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius}°C is equal to {fahrenheit:.2f}°F.")
        elif choice == 'F':
            fahrenheit = prompt_for_fahrenheit()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"\n{fahrenheit}°F is equal to {celsius:.2f}°C.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\nThank you for using the Temperature Converter Program!")
        print("\nGoodbye!\n")


if __name__ == "__main__":
    # Main function to execute the Celsius to Fahrenheit or Fahrenheit to Celsius conversion
    main()

# This code allows the user to convert temperatures between Celsius and Fahrenheit.
# It prompts the user to enter a temperature and choose the conversion direction.
# The program handles invalid inputs gracefully and provides a user-friendly interface.
# The user can convert from Celsius to Fahrenheit or from Fahrenheit to Celsius.



