# Problem 3 Solution

To solve this problem, first realize that the largest possible prime factor
for any number n is sqrt(n). This puts an upper limit on the largest possible
prime factor. The first non-trivial prime factor is 2, so for each value i
from 2 to sqrt(n), divide out those factors from n. The remaining value is
the largest prime factor.
