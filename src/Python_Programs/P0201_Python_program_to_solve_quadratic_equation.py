#A Python program to solve a quadratic equation
#Standard form of a quadratic equation is ax^2 + bx + c = 0
# where a, b, and c are constants and x is the variable.

def prompt_for_coefficients() -> tuple[float, float, float]:
    """
    Prompt the user for the coefficients of the quadratic equation.
    
    :return: Tuple containing coefficients (a, b, c)
    """
    try:
        a = float(input("Enter coefficient a (non-zero): "))
        # Ensure 'a' is not zero to avoid division by zero in the quadratic formula
        # If 'a' is zero, raise an error to prompt the user again
        if a < float('-inf') or a > float('inf'):
            raise ValueError("Coefficient 'a' must be a finite number.")
        elif a == 0:
            raise ValueError("Coefficient 'a' cannot be zero.")
        b = float(input("Enter coefficient b: "))
        if a < float('-inf') or a > float('inf'):
            raise ValueError("Coefficient 'a' must be a finite number.")
        c = float(input("Enter coefficient c: "))
        if a < float('-inf') or a > float('inf'):
            raise ValueError("Coefficient 'a' must be a finite number.")
        return a, b, c
    except ValueError as e:
        print(f"Invalid input: {e}")
        return prompt_for_coefficients()

def solve_quadratic(a: float, b: float, c: float) -> tuple[float, float, str]:
    """
    Solve the quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
    
    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant term
    :return: Tuple containing the two solutions (x1, x2)
    """

    # Calculate the discriminant
    # The discriminant is b^2 - 4ac, which determines the nature of the roots
    # If the discriminant is positive, there are two distinct real solutions.
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        #Complex roots
        type_of_solution = "Complex"
        # Calculate the real and imaginary parts of the complex solutions
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant)**0.5 / (2 * a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j, type_of_solution)  # Two complex solutions
    elif discriminant == 0:
        # One real solution (double root)
        type_of_solution = "Real and equal"
        # Calculate the single solution using the quadratic formula
        x = -b / (2 * a)
        return (x, x, type_of_solution)  # One real solution (double root)
    else:
        # Two distinct real solutions
        type_of_solution = "Real and distinct"
        # Calculate the two solutions using the quadratic formula
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return (x1, x2, type_of_solution)  # Two distinct real solutions

def print_solutions(x1: float, x2: float, type_of_solution: str) -> None:
    """
    Print the solutions of the quadratic equation.
    
    :param solutions: Tuple containing the solutions (x1, x2)
    """
    if type_of_solution == "Complex":
        print(f"The solutions are complex: {x1} and {x2}")
    elif type_of_solution == "Real and equal":
        print(f"The solution is a double root: {x1} (both roots are equal)")
    else:
        print(f"The solutions are real and distinct: {x1} and {x2}")

def main():
    """
    Main function to execute the quadratic equation solver.
    """
    a, b, c = prompt_for_coefficients()
    x1, x2, type_of_solution = solve_quadratic(a, b, c)
    print_solutions(x1, x2, type_of_solution)

if __name__ == "__main__":
    main()

# This code prompts the user for the coefficients of a quadratic equation,
# solves the equation using the quadratic formula, and prints the solutions.