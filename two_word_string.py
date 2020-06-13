# Write a function that takes a two word string and returns True if both start with the same letter


def animal_cracker(text):
    string = text.split()

    if len(string) == 2:
        first = string[0]
        second = string[1]

        if first[0].lower() == second[0].lower():
            print(True)
        else:
            print(False)
    else:
        print('Please provide two word string')
        



animal_cracker(input('Enter a two word string '))
