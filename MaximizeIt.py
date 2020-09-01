## You are given a function f(x) = x ** 2. You are also given k lists.
## The ith list consists of ni elements.
## You have to pick one element from each list so that the value from the equation below is maximized:
## s = (f(x1) + f(x2) + ... + f(xk))%m

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
