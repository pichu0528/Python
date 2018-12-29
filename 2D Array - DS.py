'''
Code challenge from HackerRank
Practice > Data Structures > Arrays > 2D Array - DS
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # method 1: using two for loops and a list to store the result, then return the max of the result list
    # total = []
    # for x in range(4):
    #     for y in range(4):
    #         sum = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
    #         total.append(sum)
    # return max(total)
    
    # method 2: similar concept as method 1, but using list comprehension.
    return max([arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2] for x in range(4) for y in range(4)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
