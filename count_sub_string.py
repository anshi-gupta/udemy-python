# program to count the substring inside a string

s = input("The string is ").strip()
sb = input("The substring is ").strip()
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print ("Number of substrings present in the string: ", results)