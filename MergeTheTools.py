## The first line contains a single string denoting s.
## The second line contains an integer, k, denoting the length of each subsegment.

## Print (n/k) lines where each line i contains string ui.
## Sample Input:      AABCAAADACDD
##                    3   
## Sample Output:
##                    AB
##                    CA
##                    AD 

def merge_the_tools(string, k):
    n = len(string)
    j = 0
    while j < n:
        u = ''
        if n % k == 0:
            for i in range(k):
                if string[j] not in u:
                    u = u + string[j]
                    j += 1
                else:
                    j += 1
        
            print(u)

string, k = input(), int(input())
merge_the_tools(string, k)