'''
Code challenge from HackerRank
Under python -> built-ins
'''


#!/bin/python3

import math
import os
import random
import re
import sys

def take_k(elem):
    return elem[k]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_list = sorted(arr,key=take_k)
    for i in sorted_list:
        print(*i)
