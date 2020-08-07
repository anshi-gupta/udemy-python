import textwrap
string = input("The string: ")
max_width = int(input("Provide width: "))
def wrapped_string(string, max_width):
  return textwrap.fill(string, max_width)
result = wrapped_string(string, max_width)
print(result)