'''
Enter a number and have the program generate π (pi) up to that many decimal places. 
Keep a limit to how far the program will go.
'''

# Method 1: Using a list
# Doesn't round up the result
from math import pi
pi_str = str(pi)
pi_list = ['3','.']

num_decimals = int(input('How many decimals: '))

for x in range(2,num_decimals+2):
    pi_list.append(pi_str[x])

print(''.join(pi_list))

# Method 2: format string
# Does round up the result
num_decimals = int(input('How many decimals: '))
print('{:.{}f}'.format(pi,num_decimals))
