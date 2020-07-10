def new_decorator(orig_func):

  def wrap_func():
    print('Some extra code, before the original func')
    orig_func()
    print('Some extra code, after the original func')
  return wrap_func

def func_needs_decorator():
  print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()