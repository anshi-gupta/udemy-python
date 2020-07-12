
f = open("HarryPotter.txt", "r+")
word_count = {}
for word in f.read().split():
  if word not in word_count:
    word_count[word] = 1

  else:
    word_count[word] +=1

for k,v in word_count.items():
  print(k, v)
f.close()