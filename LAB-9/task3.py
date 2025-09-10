"""
calculator.py

A simple calculator module that provides basic arithmetic operations: addition, subtraction, multiplication, and division.

This module allows users to perform calculations by reading input values from the console. Each function is documented with both a manually written docstring (NumPy style) and an AI-generated docstring for comparison.

Functions
---------
add(a, b)
    Returns the sum of two numbers.
subtract(a, b)
    Returns the difference between two numbers.
multiply(a, b)
    Returns the product of two numbers.
divide(a, b)
    Returns the quotient of two numbers.

Example
-------
>>> add(2, 3)
5
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The sum of a and b.

    Examples
    --------
    >>> add(2, 3)
    5
    """
    # AI-generated docstring:
    # """Returns the sum of two numbers a and b."""
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float
        The number from which to subtract.
    b : float
        The number to subtract.

    Returns
    -------
    float
        The result of a minus b.

    Examples
    --------
    >>> subtract(5, 2)
    3
    """
    # AI-generated docstring:
    # """Returns the result of subtracting b from a."""
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.

    Returns
    -------
    float
        The product of a and b.

    Examples
    --------
    >>> multiply(2, 4)
    8
    """
    # AI-generated docstring:
    # """Returns the product of two numbers a and b."""
    return a * b

def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float
        The numerator.
    b : float
        The denominator.

    Returns
    -------
    float
        The result of a divided by b.

    Raises
    ------
    ValueError
        If b is zero.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    """
    # AI-generated docstring:
    # """Returns the result of dividing a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        else:
            print("Invalid operation.")
            exit(1)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Docstring Comparison ---")
    print("Manual module docstring:\n", __doc__)
    print("\nManual function docstring for 'add':\n", add.__doc__)
    print("\nAI-generated function docstring for 'add':\n Returns the sum of two numbers a and b.")
