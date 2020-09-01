## You are given a string s. Suppose a character 'c' occurs consecutively x times in the string. 
## Replace these consecutive occurrences of the character 'c' with (x, c) in the string.

from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
