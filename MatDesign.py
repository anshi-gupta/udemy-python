# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.


def top_design(rows, columns):
  width = columns
  j = 1
  for i in range(0, int(rows / 2)):
    result = (".|." * j).center(width, "-")
    print(result)
    j += 2

def doormat_greet(rows, columns):
  name = "WELCOME"
  print(name.center(columns, "-"))

def bottom_design(rows, columns):
  width = columns
  j = rows
  for i in range(0, int((rows / 2)+1)):
    j -= 2
    while j >= 1:
      result = (".|." * j).center(width, "-")
      print(result)
      break  

a = True
while a:
  r = input().strip().split(" ")
  N = int(r[0])
  M = int(r[1])

  if N % 2 == 0:
    a = True
  else:
    top_design(N, M)
    doormat_greet(N, M)
    bottom_design(N, M)
    a = False

  