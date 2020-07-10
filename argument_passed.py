def hello():
  return "Hello"
def other(some_def_func):
  print('Other code runs here! ')
  print(some_def_func())

other(hello)