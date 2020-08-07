# to check whether string has any alphanumeric, alphabetical characters or digit or any letter is in lowercase or uppercase
s = input("The given string is ")
for i in range(0, len(s)):
  if s[i].isalnum() == True:
    result = True
    break
  else:
    result = False
print("The given string has alphanumeric character. This statement is ", result)

for i in range(0, len(s)):
  if s[i].isalpha() == True:
    result = True
    break
  else:
    result = False
print("The given string has alphabet. This statement is ", result)

for i in range(0, len(s)):
  if s[i].isdigit() == True:
    result = True
    break
  else:
    result = False
print("The given string has digit. This statement is ", result)

for i in range(0, len(s)):
  if s[i].islower() == True:
    result = True
    break
  else:
    result = False
print("The given string has any letter in lowercase. This statement is ", result)

for i in range(0, len(s)):
  if s[i].isupper() == True:
    result = True
    break
  else:
    result = False
print("The given string has any letter in uppercase. This statement is ", result)