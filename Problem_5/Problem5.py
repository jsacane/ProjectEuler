"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

n = 20

while True:
    if ((n % 19 == 0) and (n % 18 == 0) and (n % 17 == 0) and
        (n % 16 == 0) and (n % 15 == 0) and (n % 14 == 0) and
        (n % 13 == 0) and (n % 12 == 0) and (n % 11 == 0)):
        break
    else:
        n += 20

print(n)
