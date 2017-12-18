"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

largest = 0

x = 999
while x >= 100:
    y = 999
    while y >= x:
        product = x * y
        if product <= largest:
            break
        prod_string = str(product)
        if (prod_string[::-1] == prod_string):
            largest = product
        y -= 1
    x -= 1

print(largest)
