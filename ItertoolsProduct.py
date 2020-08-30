#Input Format

#The first line contains the space separated elements of list A.
#The second line contains the space separated elements of list B.

#Both lists have no duplicate integer elements

#Output Format

#Output the space separated tuples of the cartesian product.

from itertools import product
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
cartesian_list = list(product(A, B))
for i in cartesian_list:
    print(i, end = " ")
