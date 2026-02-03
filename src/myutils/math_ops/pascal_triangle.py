from math import factorial


def pascal_triangle_using_while(rows: int):
    """
    Print Pascal's Triangle with the given number of rows.
    """
    n = 0
    while n < rows:
        # Print leading spaces
        space = 1
        while space < rows - n:
            print(end=" ")
            space += 1

        # Print values in the row
        r = 0
        while r <= n:
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            print(ncr, end=" ")
            r += 1

        print()
        n += 1


def pascal_triangle(rows: int):
    for n in range(rows):
        for space in range(1, rows - n):
            print(end=" ")

        for r in range(n + 1):
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            print(ncr, end=" ")

        print("")
