from .calc import add, subtract, multiply, divide
from .adv_calc import power, modulus
from .bmi import calculate_bmi
from .prime_checker import isPrime
from .sum_natural_nums import summation

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "modulus",
    "calculate_bmi",
    "isPrime",
    "summation",
]

"""
Scripts like:

guess_the_num.py

pascal_triangle.py

→ should not be in __init__.py (they are practice / procedural).
"""
