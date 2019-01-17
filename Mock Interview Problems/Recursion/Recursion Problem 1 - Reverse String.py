'''
Reverse a String
This interview question requires you to reverse a string using recursion. 
Make sure to think of the base case here.
'''

# Solution 1
def reverse1(s):
    
    # base case: when we have one letter left or empty string
    if len(s) <= 1:
        return s
        
    # grab the last letter of the string and concatenate with the recursive result without the 
    # last letter
    return s[-1] + reverse(s[:len(s)-1])
        
# Solution 2 - similar to Solution 1, but the way we construct the return statement is different
def reverse2(s):
    
    # base case
    if len(s) <= 1:
        return s
        
    # recursion
    return reverse(s[1:]) + s[0]
        
'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print('PASSED ALL TEST CASES!')
        
# Run Tests
test = TestReverse()
test.test_rev(reverse1)
test.test_rev(reverse2)
