## Task
## You are given a complex z. Your task is to convert it to polar coordinates.

## Input Format

## A single line containing the complex number z. 
## Note: complex() function can be used in python to convert the input as a complex number.

## Constraints

## Given number is a valid complex number

## Output Format

## Output two lines:
## The first line should contain the value of phase angle.
## The second line should contain the value of modulus.

import re
import cmath
coordinate = input()
z = re.findall("\d+", coordinate)
a = int(z[0])
b = int(z[1])
first_minus = coordinate.find('-', 0, 1)
last_minus = coordinate.find('-', 1)
c1 = coordinate[first_minus]
c2 = coordinate[last_minus]
if '-' in c1 and '-' in c2:
    a = 0 - a
    b = -b

elif '-' in c1:
    a = -a
    b = b

elif '-' in c2:
    a = a
    b = -b

else:
    a = a
    b = b

print(abs(complex(a, b)))
print(cmath.phase(complex(a, b)))
