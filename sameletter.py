### Write a function that takes a two word string and returns True if both words begin with same letter

def word(mystring1,mystring2):
    first_word = mystring1[0].lower()
    sec_word = mystring2[0].lower()
    if first_word == sec_word:
        print(True)
    else:
        print(False)
word('nshi','Avinav')