"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import ceil, sqrt

def isPrime(x):
    upperBound = ceil(sqrt(x)) + 1
    return (n > 1) and (all(x % i for i in range(2, upperBound)))

n = 3
prime = 1

while prime < 10001:
    if isPrime(n):
        prime += 1
    n += 2

print(n - 2)
