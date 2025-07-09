# Python program to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

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

def main():
    """
    Main function to execute the Celsius to Fahrenheit or Fahrenheit to Celsius conversion.
    """
    choice = prompt_conversion_choice()
    
    if choice == 'C':
        celsius = prompt_for_celsius()
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == 'F':
        fahrenheit = prompt_for_fahrenheit()
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")


if __name__ == "__main__":
    # Main function to execute the Celsius to Fahrenheit or Fahrenheit to Celsius conversion
    main()
# This code allows the user to convert temperatures between Celsius and Fahrenheit.


