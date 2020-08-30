#Task
#You are given a string s.
#Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

#Input Format
#A single line containing the string s and integer value k separated by a space.
#The string contains only UPPERCASE characters.

#Output Format
#Print the different combinations of string s on separate lines.

from itertools import combinations
string = input()
s = sorted(string.split()[0])
k = int(string.split()[1])

for i in range(1, k+1):
    mylist = list(combinations(s, i))
    for j in mylist:
        print("".join(j))

