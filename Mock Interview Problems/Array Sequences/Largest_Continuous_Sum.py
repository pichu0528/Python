'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''

# My solution 1 - use a temp value to store the sum of the continuous values.
#                 After each addition of n, check two things
#                 1. If n > temp(after adding n to temp), then we remove the temp value and 
#                    and start adding from the n.
#                 2. If temp > maxsum, then we assign the temp value to maxsum.
#                 Time complexity: O(N)
#                 Note: I have the temp_arr to keep tracking of the starting and ending point
def large_cont_sum1(arr): 
    temp = 0
    maxsum = 0
    temp_arr = []
    
    for n in arr:
        temp += n
        
        if n > temp:
            temp = n
            temp_arr = []
            temp_arr.append(n)
        if temp > maxsum:
            maxsum = temp
            temp_arr.append(n)
    #return temp_arr[0],temp_arr[-1]
    return maxsum

# My solution 2 - similar to solution 1. But, using built-in function max() instead of the if 
#                 statement. And, instead of initializing the temp and maxsum value to 0.
#                 I set the values of both to the first value in the given array.
#                 Time complexity: O(N)
def large_cont_sum2(arr):
    
    # edge case check
    if len(arr) == 0:
        return 0
    
    # assign the first value of the given array to maxsum and temp
    maxsum = temp = arr[0]
    
    # since we already assign the first element of the given array to the temp and maxsum variables,
    # we will start checking from index 1.
    for n in arr[1:]:
        temp = max(temp+n,n)      # if temp+n > n, assign temp+n as the new temp value
        
        maxsum = max(temp,maxsum) # if temp > maxsum, assign temp as the new maxsum value
        
    return maxsum

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum1)
t.test(large_cont_sum2)
