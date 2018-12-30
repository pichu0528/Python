'''
Anagram Check
Problem
Given two strings, check to see if they are anagrams. 
An anagram is when the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''
# My solution 1 - compare the result for each string if they have the same characters in sorted order
def anagram(s1,s2):
    s1_list = list(''.join(s1.lower().split()))
    s2_list = list(''.join(s2.lower().split()))
    
    if sorted(s1_list) == sorted(s2_list):
        return True
    else:
        return False

# My solution 2 - using two dictionaries to keep the count of each character from each string, 
#                 and compare the counts of each character
def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    s1_dict = dict()
    s2_dict = dict()
    
    for a in s1:
        if not a in s1_dict:
            s1_dict[a] = 1
        else:
            s1_dict[a] += 1
    
    for b in s2:
        if not b in s2_dict:
            s2_dict[b] = 1
        else:
            s2_dict[b] += 1
            
    for c in s1_dict:
        try:
            if s1_dict[c] == s2_dict[c]:
                continue
            else:
                return False
        
        except Exception:
            return False
    return True

# My solution 3 - using one dictionary to keep count. Subtract the count if the character exists in the second string.
#                 If the character doesn't exist in the dictionary, add the character as a key and give a count 1.
#                 Check the count dictionary to see if all the values are equal to 0. If not, then return False
def anagram3(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # check for edge case - different length, return False
    if len(s1) != len(s2):
        return False
    
    count = {} # dictionary to keep count for s1
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    # decrement the count by 1 if the character also exists in s2
    # if the character doesn't exist in count, add the character with
    # count 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # go through the keys in count, check if the value == 0
    # if not, then it is not an anagram
    for k in count:
        if count[k] != 0:
            return False
        
    return True
        
'''
RUN THIS CELL TO TEST YOUR SOLUTION
'''
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print "ALL TEST CASES PASSED"

# Run Tests
t = AnagramTest()
t.test(anagram)
