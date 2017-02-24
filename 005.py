"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
# turns out my math sucks
# don't know how to solve this problem mathematically
# so I take look at other's code here 
# http://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

def solution(step, check_list):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

check = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(solution(2520, check))