#Python program to convert kilometers to miles
def km_to_miles(km: float) -> float:
    # 1 kilometer is approximately equal to 0.621371 miles
    return km * 0.621371

def print_conversion(km: float) -> None:
    miles = km_to_miles(km)
    print(f"{km} kilometers is equal to {miles:.2f} miles.")

if __name__ == "__main__":
    try:
        km = float(input("Enter distance in kilometers: "))
        print_conversion(km)
    except ValueError:
        print("Please enter a valid number.")
# Example usage:
# Enter distance in kilometers: 5
# 5 kilometers is equal to 3.11 miles.