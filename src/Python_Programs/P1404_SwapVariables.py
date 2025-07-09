# Swap two variables in Python

def swap_variables(a, b):
    """
    Swap two variables using a temporary variable.
    
    :param a: First variable
    :param b: Second variable
    :return: Tuple containing swapped values (b, a)
    """
    temp = a
    a = b
    b = temp
    #print(f"Swapped values: a = {a}, b = {b}")
    return a, b
