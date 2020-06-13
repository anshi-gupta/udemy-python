# Write a function that capitalizes first and fourth letter of a word

def old_macdonald(word):
    first_letter = word[0].upper()
    fourth_letter = word[3].upper()
    new_string = ""
    i = 0

    while i<len(word):
        if i == 0:
            new_string += first_letter
            i += 1

        elif i == 3:
            new_string += fourth_letter
            i += 1

        else:
            new_string += word[i].lower()
            i += 1

    print(new_string)

old_macdonald('Macdonald')
old_macdonald('macdonald')
old_macdonald('MACDONALD')
