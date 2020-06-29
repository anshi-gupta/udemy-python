
def ask():
  while True:
    try:
      num = int(input("Input an integer: "))
      square = num**2
    except:
      print("An error occured! Please try again.")
      continue
    else:
      print("Thank you! The number squared is ", square)
      break

ask()