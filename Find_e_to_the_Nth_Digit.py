'''
Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
'''

# Method 1: Using a list
# Doesn't round up the result
from math import e
e_str = str(e)
e_list = ['2','.']

num_decimals = int(input('How many decimals: '))

for x in range(2,num_decimals+2):
    e_list.append(e_str[x])

print(''.join(e_list))

# Method 2: format string
# Does round up the result
num_decimals = int(input('How many decimals: '))
print('{:.{}f}'.format(e,num_decimals))
