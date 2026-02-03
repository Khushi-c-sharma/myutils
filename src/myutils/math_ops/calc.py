def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of two numbers (a / b).

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    try:
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))
    except ValueError:
        print("Please enter valid numbers.")
        exit()

    print(
        """Operations available: \n
        1. Addition\n
        2. Subtraction\n
        3. Multiplication\n
        4. Division"""
    )

    selection = int(input("Enter the serial number of the operation to be performed: "))

    if selection == 1:
        print(f"{a} + {b} = {add(a, b)}")
    elif selection == 2:
        print(f"{a} - {b} = {subtract(a, b)}")
    elif selection == 3:
        print(f"{a} x {b} = {multiply(a, b)}")
    elif selection == 4:
        print(f"{a} ÷ {b} = {divide(a, b)}")
    else:
        print("Invalid option selected.")
