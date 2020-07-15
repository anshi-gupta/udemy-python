import random
random.randint(1, 10)

def rand_num(low, high, n):
  for x in range(n):
    yield random.randint(low, high)
for num in rand_num(1, 10 , 12):
  print(num)
