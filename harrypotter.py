
f = open("HarryPotter.txt", "r+")
word_count = {}

punc = '.,!_-:;"?/(){}[]'
no_punc = ""
for char in f.read():
  if char not in punc:
    no_punc = no_punc + char

for word in no_punc.split():
  if word not in word_count:
    word_count[word] = 1

  else:
    word_count[word] +=1

for k,v in word_count.items():
  print(k, v)
f.close()