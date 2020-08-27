## You are given two sets, A and B..
## Your job is to find whether set A is a subset of set B.

## If set A is subset of set B, print True.
## If set A is not a subset of set B, print False.

## Input Format

## The first line will contain the number of test cases, T.
## The first line of each test case contains the number of elements in set A .
## The second line of each test case contains the space separated elements of set A.
##The third line of each test case contains the number of elements in set B.
##The fourth line of each test case contains the space separated elements of set B.

## Outout Format
## Output True or False for each test case on separate lines.

## The first line will contain the number of test cases, T.
T = int(input())

def checkSubset():
    if set_A.issubset(set_B) == True:
        print(True)
    else:
        print(False)

for i in range(T):
    ## The first line of each test case contains the number of elements in set A .
    ## The second line of each test case contains the space separated elements of set A.
    A, set_A = int(input()), set(map(int, input().split()))

    ## The third line of each test case contains the number of elements in set B.
    ## The fourth line of each test case contains the space separated elements of set B.
    B, set_B = int(input()), set(map(int, input().split()))

    checkSubset()