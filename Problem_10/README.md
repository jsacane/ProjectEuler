# Problem 10 Solution

## Problem10.py
This solution uses an optimized "check divisors" approach similar to problem 7.
It checks all odd numbers if they're prime by division testing up to sqrt(n).

## Problem10_better.py
This solution uses the "sieve of Eratosthenes" method. It is an iterative process
that uses extra memory to ignore all multiples of primes. The method can be
optimized to avoid using even numbers, halving the amount of extra space and
decreasing cache misses, thereby increasing performance. If the i'th value of
the array is an odd number 2i + 1, then (2i + 1)^2 has index 2i(i+1). So, if
the i'th value is prime, then start at 2i(i+1) and proceed with steps of
2i + 1 to mark its multiples as primes.
