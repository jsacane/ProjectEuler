"""
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import ceil, sqrt

def isPrime(x):
    upperBound = ceil(sqrt(x)) + 1
    return (n > 1) and (all(x % i for i in range(2, upperBound)))

n = 3
sum = 2

while n < 2000000:
    if isPrime(n):
        sum += n
    n += 2

print(sum)
