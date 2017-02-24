"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

import math


def findprime(n_th):
    '''find the n th prime'''
    if n_th == 1:
        return 2
    if n_th == 2:
        return 3
    count = 2
    n = 3
    while count < n_th:
        n += 1
        sqrt = int(math.floor(n**0.5))
        # there is no need to check from 2 to n-1
        # only those less than or equal to sqrt(n) is enough
        if all(n % s != 0 for s in range(2, sqrt + 1)):
            count += 1
    return n

print(findprime(10001))
