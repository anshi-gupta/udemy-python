## Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
## You are given n scores. Store them in a list and find the score of the runner-up.

## The first line contains n. The second line contains an array A[] of n integers each separated by a space.
## Constraints: 
##             2<=n<=10
##             -100<=A[i]<=100

## Print the runner-up score.

# n = number of inputs
n = int(input())

# string to store n number of inputs
string = input()

# converts n number of elements of string into integer and separates them by space
array = [int(s) for s in string.split() if len(string.split()) == n]

# gives the maximum value of the array
mx = max(array)

if mx in array:
    new_list = set(array)
    new_list.remove(mx)

print(max(new_list))


