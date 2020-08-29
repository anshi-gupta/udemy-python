##  Given a right angled triangle ABC.
##  M is the mid-point of hypothenus,AC.
##  INPUT - The other two sides of the triangle ABC, AB and BC.
##  OUTPUT - Angle MBC

import math
AB = int(input())
BC = int(input())
AC = math.hypot(AB, BC)
MC = AC / 2
MBC = math.acos(0.5 * BC/MC)
result = math.degrees(MBC)
print(round(result), end = u'\N{DEGREE SIGN}')

