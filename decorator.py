def hello(name = "Anshi"):
  print('The hello() function has been executed')
  def greet():
    return '\t This is the greet () func inside hello'
  print(greet())
hello()