"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispalindrome(n):
    n = str(n)
    r = ''
    for digit in n:
        r = digit + r
    if n == r:
        return True
    else: return False

i = 999
while not ispalindrome(i*999):
    i -= 1
    if i < 100:
        print 'Oh no'
        break
print i*999
