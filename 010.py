"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

l = [17]
n = 7
while n <= 2000000:
    n += 1
    sqrt = int(math.floor(n**0.5))
    if all(n % s != 0 for s in range(2, sqrt + 1)):
        l.append(n)
print(sum(l))
