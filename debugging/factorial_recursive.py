#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        int: The factorial of n (n!).

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the first command line argument and convert it to integer


f = factorial(int(sys.argv[1]))


# Print the result
print(f)
