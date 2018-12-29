'''
Code challenge from HackerRank under itertools
'''

from itertools import product

# n is the number of arrays
# m is the divider
n,m = map(int,input().split())
total = []

# put each array in a list
for i in range(n):
    total.append(list(map(int,input().split()))[1:])

# product(*total) - find the Cartesian product from the total list
# iterate throgh each tuple in the total list and iterate through each int in the tuple
# calculate (sum of each int ^ 2)%m from each tuple and put the result in the result list
result = (sum(num**2 for num in numbers) % m for numbers in product(*total))

print(max(result))
