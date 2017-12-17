# Problem 5 Solution

## Problem5.py

This solution uses a slightly optimized brute-force approach. n = 20 is the
largest number we can start with, since we know it is divisible by 20. If n is
divisible by 20, then we know it is also divisible by 10, 5, 4, and 2, so we
don't have to check those. Similarly if it's divisible by 18, it is also divisible
by 9, 6, and 3, etc. Therefore, we only need to check for divisibility with 19
down to 11, as their divisors form a complete set from {1, ..., 20}. If all these
conditions are met, then n is guaranteed to be the smallest multiple. Otherwise,
increment n by 20 and try again.
