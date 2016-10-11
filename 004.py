"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispalindrome(n):
    ''' return True if n is palindromic.'''
    n = str(n)
    r = ''
    for digit in n:
        r = digit + r
    if n == r:
        return True
    else: return False

def findmax():
    for a in range(1000,99,-1):
        for b in range(1000,99,-1): 
            if ispalindrome(a*b):
                print a*b, '=', a, '*', b
                return (a, b, a*b)

findmax()