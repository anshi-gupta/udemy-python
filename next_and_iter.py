# next function
def sim_gen():
  for x in range(3):
    yield x
for num in sim_gen():
  print(num)

g = sim_gen()
print("Using next function")
print("Gives the first number")
print(next(g))
print("Gives the next number")
print(next(g))
print("Gives the next number")
print(next(g))

# iter function
# str object is not an iterator 
# turn the string into generator using iter
print("\n")
print("An example of Iter function")
s = "hello"
for letter in s:
  print(letter)

print("After using iter function")
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))