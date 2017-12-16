# Problem 2 Solution

## Problem2.py
This solution uses a simple iterative approach. Given the first two values of
the sequence (1 and 2), the subsequent values can be constructed and tested
for even-ness. If the current value of the sequence is even, add it to the
running sum.

## Problem2_better.py
This solution eliminates the need for explicitly checking if the number is
even by taking advantage of the fact that every 3rd Fibonacci number is even.

Proof by induction:

Let F(n) = F(n - 1) + F(n - 2), F(0) = F(1) = 1.

The first third number in the sequence is at n = 2.

By the definition above, F(2) = F(1) + F(0) = 1 + 1 = 2, which is even.

Now assume F(k) is even for some k >= 2. F(k + 3) = F(k + 2) + F(k + 1).

Since we know F(k) is even, then F(k + 1) is odd. Also, F(k + 2) = F(k + 1) + F(k).

Since F(k) is even and F(k + 1) is odd, then F(k + 2) is an odd integer plus an
even integer, which is always an odd integer.

Therefore, F(k + 3) is an odd integer plus an odd integer which is always an
even integer, so F(k + 3) is even.

Q.E.D
