
n = int(input())
binary = "{0:b}"
l = len(binary.format(n))

for i in range(1, n+1):
    dec = "{0:d}"
    oct = "{0:o}"
    hex = "{0:X}"
    binary = "{0:b}"
    print(dec.format(i).rjust(l), oct.format(i).rjust(l), hex.format(i).rjust(l), binary.format(i).rjust(l))




