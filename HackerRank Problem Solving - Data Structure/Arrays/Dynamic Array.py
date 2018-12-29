'''
Code challenge from HackerRank
Practice > Data Structures > Arrays > Dynamic Array
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    last_answer = 0
    result = []
    #create n number of seq array
    # for _ in range(n):
    #     seq_list.append([])
    seq_list = [[] for _ in range(n)]

    for i in queries:
        seq = (i[1]^last_answer)%n
        if i[0] == 1: 
            seq_list[seq].append(i[2])
        elif i[0] == 2:
            last_answer = seq_list[seq][i[2]%len(seq_list[seq])]
            result.append(last_answer)
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
