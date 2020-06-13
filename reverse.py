# Given a sentence, return a sentemce with the words reversed

def master_yoda(text):
    text_split = text.split()
    reverse_word = text_split[::-1]
    print(' '.join(reverse_word))
master_yoda('I am home')
