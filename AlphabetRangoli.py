# You are given an integer N, . Your task is to print an alphabet rangoli of size N.

# size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string
alpha = string.ascii_lowercase
pattern_list = []
boolean = True
while boolean:
    n = int(input("Enter an integer(1 to 26): "))
    if n < 27:
        for i in range(n):
            pattern = "-".join(alpha[i:n])
            pattern_list.append((pattern[::-1]+pattern[1:]).center(4*n-3, "-")) 
        boolean = False
    else:
        boolean = True
print('\n'.join(pattern_list[:0:-1]+pattern_list))
