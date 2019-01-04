'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

# My solution 1 - using OrderedDict() from collections because the order needs to be maintained.
#                 return the result by list comprehension.
import collections
def compress1(s):
    s_dict = collections.OrderedDict()
    s_list = []
    
    for c in s:
        if c not in s_dict:
            s_dict[c] = 1
        else:
            s_dict[c] += 1
    
    
    #print(*['{}{}'.format(k,v) for k,v in s_dict.items()],sep='')
    return ''.join(['{}{}'.format(k,v) for k,v in s_dict.items()])
    

# Solution 2 - Run Length Compression Algorithm

def compress2(s):
    
    r = ''
    l = len(s)
    
    # edge cases
    if l == 0:
        return ''
    if l == 1:
        return s+'1'
    
    # note: i is being set to 1 because we would like to be able to check the value of the 
    #       previous
    count  = 1
    i      = 1
    
    while i < l:
        # increment the count if the current value == the previous value
        if s[i] == s[i-1]:
            count += 1
        # else add the character and the count to the string r
        else:
            r = r + s[i-1] + str(count)
            count = 1
            
        i += 1
    
    # need to put the last character/symbol and its count to the string.
    # if this step is missing, r will only contain the characters and the counts up to the
    # second to the last character.
    r = r + s[i-1] + str(count)
    
    return r

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress1)
t.test(compress2)
