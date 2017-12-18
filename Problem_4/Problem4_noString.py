"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from math import floor

def isPalindrome(x):
    num = x
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = floor(num / 10)
    return (x == reverse)

largest = 0

x = 999
while x >= 100:
    y = 999
    while y >= x:
        product = x * y
        if product <= largest:
            break
        if isPalindrome(product):
            largest = product
        y -= 1
    x -= 1

print(largest)
