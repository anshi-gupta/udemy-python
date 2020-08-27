## You are given a set A and n other sets.
## Your job is to find whether set A is a strict superset of each of the N sets.
## Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
## A strict superset has at least one element that does not exist in its subset.

## Input Format

## The first line contains the space separated elements of set A.
## The second line contains integer n, the number of other sets.
## The next n lines contains the space separated elements of the other sets.

## Output Format
## Print True if set A is a strict superset of all other N sets. Otherwise, print False.

A = set(map(int, input().split()))
n = int(input())
new_set = set()

def checkSuperset():
    if A.issuperset(new_set) == True:
        print(True)
    else:
        print(False)

for i in range(n):
    N = set(map(int, input().split()))
    new_set.update(N)

checkSuperset()
