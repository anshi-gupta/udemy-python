
#  the yield statement is used to define generators, replacing the return of a function to provide a result to its caller without destroying local variables.
#   Unlike a function, where on each call it starts with new set of variables, a generator will resume the execution where it was left off
def gen_fibon(n):
  a = 1
  b = 1
  for i in range(n):
    yield a
    a, b = b, a+b
for num in gen_fibon(10):
  print(num)
