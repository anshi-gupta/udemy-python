
def gensquare(n):
  for x in range(n):
    yield x**2
for x in gensquare(10):
  print(x)