# Problem 7 Solution

This solution uses an optimized brute force algorithm. Since the largest prime
factor a number can have is sqrt(n) + 1, we check if the number is divisible by
any numbers from 2 to sqrt(n) + 1. If not, then it is prime. Since all primes
after 2 are odd, increment the number by 2 each time.
