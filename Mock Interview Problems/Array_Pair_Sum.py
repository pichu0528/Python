'''
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
'''

# My solution 1 - keep count for each possible combination of values, duplicates included. Divide the count by 2 at the end
def pair_sum(arr,k):
    
    count = 0
    for i in arr:
        if arr.count(k - i) > 0:
            count += 1
        else:
            continue
    return count//2
    
# My solution 2 - keep an array of combination tuples, and return the length of the array divided by 2
def pair_sum2(arr,k):
    
    pairs = []
    
    for i in arr:
        if arr.count(k-i) > 0:
            pairs.append((i,arr[arr.index(k-i)]))
        else:
            continue
    
    return len(pairs)//2
   
# My solution 3 - using set to keep track of the visited value, and store tuple result in another set.
def pair_sum3(arr,k):
    # Edge case check
    if len(arr) < 2:
        return
    # Sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)),max(num,target)))
        
    return len(output)
    # if you are being asked to print out the pairs
    # print '\n'.join(map(str,list(output)))
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum1)
t.test(pair_sum2)
t.test(pair_sum3)
