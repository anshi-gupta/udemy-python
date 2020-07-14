f = open("HarryPotter.txt", "r+")
word_count = {}

punc = '''.,!_-:;"?/(){}[]'''
no_punc = ""
z = ""

for char in f.read():
  if char not in punc:
    no_punc = no_punc + char

for word in no_punc.split():
    if word[0] == "'":
      first = word[1:]
      z = z + first.lower() + " "
    elif word[-1] == "'":
      last = word[:-1]
      z = z + last.lower() + " "
    else:
      no_apostrophe = word
      z = z + no_apostrophe.lower() + " "

for word_new in z.split():
  if word_new not in word_count:
    word_count[word_new] = 1

  else:
    word_count[word_new] +=1

for k,v in word_count.items():
  print(k, v)

f.close()