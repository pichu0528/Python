'''
Consider an array of non-negative integers. A second array is formed by shuffling the elements of 
the first array and deleting a random element. Given these two arrays, find which element is missing 
in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the 
second array.

Input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5 is the missing number
'''

# My solution 1 - using a dictionary to keep track the number of each character/integers in arr1. 
#                 Then, subtract the count by comparing the dictionary to arr2.
#                 The result will be the character/integer that still has 1 count.
#                 Time complexity: O(N + N + N) = O(3N) => O(N)
def finder1(arr1,arr2):
    
    num = dict()
    
    for i in arr1:
        if i not in num:
            num[i] = 1
        else:
            num[i] += 1
            
    for j in arr2:
        if j in num:
            num[j] -= 1
            
    for c in num:
        if num[c] != 0:
            return c
            
 # My solution 2 - sort out both of the arrays first. Then, zip them together, O(logN)
 #                 Compare the two numbers in the tuple by tuple unpacking. 
 #                 Return the last element in arr1 if can't find the number in the array of tuples.
 #                 Time complexity: O(NlogN)
 def finder2(arr1,arr2):
    
    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    
    return arr1[-1]
            
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder1)
t.test(finder2)
