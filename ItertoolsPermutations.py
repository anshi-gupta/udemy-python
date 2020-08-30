#Input Format
#A single line containing the space separated string  and the integer value .
#The string contains only UPPERCASE characters.

#Output Format
#Print the permutations of the string  on separate lines.

from itertools import permutations
string = input()
s = list(string.split()[0].upper())
k = int(string.split()[1])

mylist = list(permutations(s, k))
mylist.sort()
for i in mylist:
    print("".join(i))
