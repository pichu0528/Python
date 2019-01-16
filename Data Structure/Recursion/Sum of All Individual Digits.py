'''
Given an integer, create a function which returns the sum of all the individual digits in that 
integer. 

For example: if n = 4321, return 4 + 3 + 2 + 1 = 10
'''
def sum_func(n):
    
    # base case: when n < 10 return n
    if n < 10:
        return n
    else:
        print(n)
        return n%10 + sum_func(n//10)
