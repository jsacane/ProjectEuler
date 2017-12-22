"""
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

bound = (2000000 - 1) // 2            # number of odds below 2000000
sieve = [False] * (bound+1)           # array giving which numbers are prime
limit = int((sqrt(2000000) - 1) // 2) # number of values that need to be checked

for i in range(1, limit+1):
    if not sieve[i]:                  # 2*i + 1 is prime, mark multiples as not prime
        for j in range(2*i*(i+1), bound+1, 2*i+1):
            sieve[j] = True

sum = 2
for i in range(1, bound+1):
    if not sieve[i]:
        sum += 2*i + 1

print(sum)
