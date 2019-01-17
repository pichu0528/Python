'''
Write a recursive function which takes an integer and computes the cumulative sum of 0 to that 
integer.

For example, if n = 4 , return 4 + 3 + 2 + 1 + 0, which is 10.

This problem is very similar to the factorial problem
Remember, always think of what the base case will look like. In this case, we have a base case of 
n = 0
'''

def rec_sum(n):
    
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)
