'''
Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of
parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the
string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, 
balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
'''

# Solution 1 - use LIFO data structure to solve for this problem.
#              Time complexity: O(N)
def balance_check1(s):
    temp = [] # going to behave like a stack
    
    # edge case: the length of s needs to be an even number
    if len(s) % 2 != 0:
        return False
    
    for i in range(len(s)):
        # append all the opening brackets to the temp stack
        if s[i] == '[' or s[i] == '{' or s[i] == '(':
            temp.append(s[i])
        # if temp is empty, return False
        elif len(temp) == 0:
            return False
        # if we encountered one of the closing tag, pop the value from the stack and compare
        elif s[i] == ']':
            if ord(temp.pop()) + 2 == ord(s[i]):
                continue
            else:
                return False
        elif s[i] == '}':
            if ord(temp.pop()) + 2 == ord(s[i]):
                continue
            else:
                return False
        elif s[i] == ')':
            if ord(temp.pop()) + 1 == ord(s[i]):
                continue
            else:
                return False
            
    return True
    
# Solution 2 - cleaner way, and made use of sets for checking opening brackets and matching
#              brackets.
#              Time complexity: O(N)
def balance_check2(s):
    
    if len(s) % 2 != 0:
        return False
    
    # use a set for opening brackets
    opening = set('({[')
    # use a set for matching pairs of brackets
    matches = set([('(',')'),('{','}'),('[',']')])
    # the stack we are going to use
    stack = []
    
    for paren in s:
        # if current is an opening bracket, push to the stack
        if paren in opening:
            stack.append(paren)
        # else, we encountered a closing bracket
        else:
            if len(stack) == 0:
                return False
            # pop off the last value from the stack
            last_open = stack.pop()
            # if the tuple of last value and current value not in
            # the set of tuples, return False
            if (last_open,paren) not in matches:
                return False
    # if the length of the stack is 0, meaning we have gone through
    # the string, s, and paired up all the opening and closing
    # brackets.
    return len(stack) == 0
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check1)
t.test(balance_check2)
