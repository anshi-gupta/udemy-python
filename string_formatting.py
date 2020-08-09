
n = int(input())
binary = "{0:b}"
l = len(binary.format(n))

for i in range(1, n+1):
    dec = "{0:d}"
    octal = "{0:o}"
    hexa = "{0:X}"
    binary = "{0:b}"
    print(dec.format(i).rjust(l), octal.format(i).rjust(l), hexa.format(i).rjust(l), binary.format(i).rjust(l))




