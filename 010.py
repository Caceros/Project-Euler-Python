"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

l = [2, 3]
n = 3
while True:
    if n >= 2000000:
        break
    n += 1
    sqrt = int(math.floor(n**0.5))
    if all(n % s != 0 for s in range(2, sqrt + 1)):
        l.append(n)
print sum(l)
