'''
Fibonnaci Sequence
In this interview excercise we will begin to get a feel of having to solve a single problem 
multiple ways!

Problem Statement
Implement a Fibonnaci Sequence in three different ways:

Recursively
Dynamically (Using Memoization to store results)
Iteratively

Function Output
Your function will accept a number n and return the nth number of the fibonacci sequence

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking 
to see if n = 0 or 1, then it returns 1.
'''

# Recursively
def fib_rec(n):
    
    if 0 <= n <= 1:
        return n
    
    return fib_rec(n-1) + fib_rec(n-2)
    
# Dynamically - with memoization

memoization = {}

def fib_dyn(n):
    
    # base case
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    if not n in memoization:
        memoization[n] = fib_dyn(n-2) + fib_dyn(n-1)
        
    return memoization[n]

# Iteratively - Solution 1
def fib_iter1(n):
    result = [1,1]
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return 'Can\'t use a negative number'
    
    for i in range(2,n):
        result.append(result[i-1]+result[i-2])
        
    return result[-1]

# Iteratively - Solution 2
def fib_iter2(n):
    
    a, b = 0, 1
    
    for i in range(n):
        a, b = b, a+b
        
    return a

"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib_rec)
t.test(fib_dyn) # Note, will need to reset cache size for each test!
t.test(fib_iter1)
t.test(fib_iter2)
