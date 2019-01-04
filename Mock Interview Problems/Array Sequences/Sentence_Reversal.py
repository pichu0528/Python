'''
Given a string of words, reverse all the words. For example:

Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. 
So that inputs such as:
'  space here'  and 'space here      '

both become:
'here space'
'''

# My solution 1: using the built-in functions.
#                split() - for string
#                '[something]'.join() - join the list together with [something] 
def rev_word1(s):
    return ' '.join(s.split()[::-1])
    
# My solution 2: using a list. Loop through the string and check for all the characters, excluding
#                the spaces. 
def rev_word2(s):
    words = []
    length = len(s)
    space = [' ']
    
    i = 0
    while i < length:
        if s[i] not in space:
            
            word_start = i
            
            while i < length and s[i] not in space:
                i+=1
            
            words.append(s[word_start:i])
        i += 1
        
    return ' '.join(reversed(words))
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word1)
t.test(rev_word2)
