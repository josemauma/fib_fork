"""
    Calculates the nth Fibonacci number.
    
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
    usually starting with 0 and 1. That is, F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1.
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If the input is a negative integer.
"""


import argparse
import sys
from functools import cache

@cache
def fibonacci_iterative(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be greater than or equal to 0")
    elif n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('nth', type=int, help='The position in the Fibonacci sequence to calculate.')
    args = parser.parse_args()
    
    result = fibonacci_iterative(args.nth)
    print(result)
