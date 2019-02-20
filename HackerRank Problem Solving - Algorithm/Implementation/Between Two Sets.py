'''
### [Challenge Name: Between Two Sets](/challenges/between-two-sets)


You will be given two arrays of integers and asked to determine all integers that satisfy the 
following two conditions:  

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being *between* the two arrays.  You must determine how many 
such numbers exist.

For example, given the arrays $a = [2, 6]$ and $b = [24, 36]$, there are two numbers between them:
$6$ and $12$.  
$6\%2 = 0$, 
$6\%6 = 0$, 
$24\%6 = 0$ and 
$36\%6 = 0$ for the first value.  
Similarly, 
$12\%2 = 0$, 
$12\%6 = 0$ and 
$24\%12 = 0$, 
$36\%12 = 0$.  

**Function Description**  

Complete the *getTotalX* function in the editor below.  It should return the number of integers 
that are betwen the sets.  

getTotalX has the following parameter(s):  

- *a*: an array of integers  
- *b*: an array of integers  
'''
#!/bin/python3

import os
import sys
from math import gcd


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #

    # find least common multiplier
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm,i)

    # find greatest common divisor
    g = b[0]
    for i in b[1:]:
        g = gcd(g,i)

    # for i in range(1,g+1):
    #     if g % i == 0 and i % lcm == 0:
    #         factor.append(i)
    factor = [i for i in range(1,g+1) if g%i==0 and i%lcm == 0]

    print(len(factor))
    return len(factor)

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
