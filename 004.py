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
    else:
        return False


def findmax(lower, upper):
    '''print the equation max = max_a * max_b
       and return max '''
    m = 0
    max_a = 0
    max_b = 0
    for a in range(lower, upper):
        for b in range(lower, upper):
            s = a * b
            if ispalindrome(s) and s > m:
                m = s
                max_a = a
                max_b = b
    # print(max_a * max_b, '=', max_a, '*', max_b)
    return(m)

print(findmax(100, 999))
# 906609 = 913 * 993
# 906609
