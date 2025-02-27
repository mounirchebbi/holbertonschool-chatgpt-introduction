#!/usr/bin/python3
import sys


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


f = factorial(int(sys.argv[1]))
print(f)
