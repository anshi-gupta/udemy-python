def hello(name = 'Anshi'):
  print('The hello() function has been executed')
  
  def greet():
    return '\t This is the greet () func inside hello'
  
  def welcome():
    return '\t This is welcome() inside hello'
  
  print('I am going to return a function!!')

  if name == 'Anshi':
    return greet
    
  else:
    return welcome
    

my_new_func = hello('Anshi')
print(my_new_func())

my_next_func = hello('Avi')
print(my_next_func())