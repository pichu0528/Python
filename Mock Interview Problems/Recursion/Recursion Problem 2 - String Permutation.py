'''
Given a string, write a function that uses recursion to output a list of all the possible 
permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx' 
would return a list with 6 "versions" of 'xxx'
'''
# Solution 1 - with counter
# Bascially, each permutation is a pair of the string s and the reverse of the string.
# example: abc -> cba, 
#          bca -> acb, 
#          cab -> bac
# So, the goal here is to find all the possible pairs. 
# We will keep a counter to keep track of how many pairs we have so far. 
# Total pair should be the factorial of len(n) divided by 2
# Will need to make sure of the math library to do the factorial count.
import math
def permute1(s, count=0):
    l = []
    
    #base case
    if count == math.factorial(len(s))/2:
        return []
    
    l.append(s)
    l.append(s[::-1])
    return sorted(l + permute1(s[1:] + s[0], count+1))


# Solution 2 - without counter
# 1. Iterate through the initial string – e.g., ‘abc’.
#
# 2. For each character in the initial string, set aside that character and get a list of all 
# permutations of the string that’s left. So, for example, if the current iteration is on 'b', 
# we’d want to find all the permutations of the string 'ac'.
#
# 3. Once you have the list from step 2, add each element from that list to the character from 
# the initial string, and append the result to our list of final results. So if we’re on 'b' 
# and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', 
# each of which we’d add to our final results.
#
# 4. Return the list of final results.
def permute2(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute2(s[:i] + s[i+1:]):
                
                # Add it to output
                out += [let + perm]

    return out
    

"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""

from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print 'All test cases passed.'
        
# Run Tests
t = TestPerm()
t.test(permute1)
t.test(permute2)
