## You are given a list of N lowercase English letters. 
## For a given integer k, you can select any k indices (assume 1-based indexing) with a uniform probability from the list.

## Find the probability that at least one of the k indices selected will contain the letter: 'a'.

from itertools import combinations
N = int(input())
c = 0
l = 0
mylist = list(input().split()[:N])
k = int(input())
comb = combinations(mylist, k)
for tuples in comb:
    if 'a' in tuples:
        print(tuples)
        c += 1
    l += 1

print(c/l)

