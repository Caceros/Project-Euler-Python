"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def maxprime(num):
    d = 2
    prime = []
    while d*d <= num:
        while num % d == 0:
            prime.append(d)
            num /= d
        d += 1
    if num > 1:
        prime.append(num)
    return int(max(prime))
print(maxprime(600851475143))
