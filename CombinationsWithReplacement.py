#Task
#You are given a string s.
#Your task is to print all possible size k replacements of the string in lexicographic sorted order.

#Input Format
#A single line containing the string s and integer value k separated by a space.
#The string contains only UPPERCASE characters.

#Output Format
#Print the combinations with their replacements of string s on separate lines.

from itertools import combinations_with_replacement
string = input()
s = sorted(string.split()[0])
k = int(string.split()[1])

mylist = list(combinations_with_replacement(s, k))
for j in mylist:
    print("".join(j))

