'''
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. 
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing)
with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format

The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists
of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints
  1. 1 <= N <= 10
  2. 1 <= K <= N
All the letters in the list are lowercase English letters.

Sample Input
4 
a a c d
2

Sample Output
0.8333

Explanation
All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6.
'''

from itertools import combinations
n = int(input())
c_list = input().split()
k = int(input())
l = list(combinations(c_list,k))

# method 1: for loop and implement count
# count = 0
# for i in l:
#     for j in i:
#         if j == 'a':
#             count+=1
#             break
# print('%.4f' %(count/len(l)))

# method 2: list comprehension to check how many sub-lists include 'a'
print('%.4f' %(len([i for i in l if i.count('a')>0])/len(l)))
