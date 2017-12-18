# Problem 4 Solution

## Problem4.py
This solution uses an optimized brute-force technique that starts at the largest
3-digit product (999 * 999) and works it way down, looking for palindromes.
If the product is already smaller than the largest palindrome, then don't bother
checking that product. Furthermore, don't check repeated products (i.e.
x * y = y * x, so don't check y * x).

## Problem4_noString.py
This solution works the same way as above, but doesn't use strings to check
for palindromes. Instead, it extracts individual digits with modulo, and builds
up a new number with the digits in reverse. If the reverse number is equal to the
original number, it's a palindrome.
