'''
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
'''

# Solution 1 - convert the string into a set. Then, compare the length of both
#              Time complexity: O(N)
def uni_char1(s):
    return len(set(s)) == len(s)
    
# Solution 2 - looping through each character and use the built-in function, count(), to check if
#              the count is greater than 1. If it is, that means there is a duplicate character.
#              Time complexity: O(N)
def uni_char2(s):
    for c in s:
        if s.count(c) > 1:
            return False
    return True
    
# Solution 3 - use a set to keep track the unique characters. If the character that we are 
#              currently checking already exists in the set, return False.
#              Time complexity: O(N)
def uni_char3(s):
    chars = set()
    
    for c in s:
        if c in chars:
            return False
        # add the character to the set if it does not exist yet, so we can use the new updated 
        # set for next check.
        else:
            chars.add(c)
    return True

"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char1)
t.test(uni_char2)
t.test(uni_char3)
