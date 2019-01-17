'''
Create a function called word_split() which takes in a string phrase and a set list_of_words. 
The function will then determine if it is possible to split the string in a way in which words 
can be made from the list of words. You can assume the phrase will only contain words found in 
the dictionary if it is completely splittable.

For example:

word_split('themanran',['the','ran','man'])
will return ['the', 'man', 'ran']

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
will return ['i', 'love', 'dogs', 'John']

word_split('themanran',['clown','ran','man'])
will return []
'''

# Solution 1 - only works when there is no symbol in the list of words.
#              Space complexity: O(N)
#              Time complexity: O(N)
def word_split(s,d):

    # append a plus sign at the end of the string
    # the '+' is going to be an indicator if we reach the end of the string
    s = [c for c in s]
    s.append('+')
    s = ''.join(s)
    
    l = []
    i = 0
    temp = ''
    
    # base case: if we see the '+' sign, we have reached the end of the string
    #            then, return blank list
    if temp == '+':
        return []
    
    while len(temp) != len(s):
        i += 1
        # if temp is in the list of words, append the value of temp to a list
        # then, we can use recursion to find the next word in the list that is
        # in the string.
        if temp in d:
            l.append(temp)
            return l + word_split(s[i-1:],d)
            
        else:
            temp = s[:i]
        
    return []
    
# Solution 2 - This is a very "python-y" solution.

def word_split(phrase,list_of_words, output = None):
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        # if phrase.startswith(word):
        if phrase[:len(word)] == word:
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- 
            # phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output
