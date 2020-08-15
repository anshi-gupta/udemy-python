# Count which player got the highest score and print the name of the player and his score.
string = input("Enter a word: ")
vowels = 'AEIOU'

# counts the number of substring starting from a vowel
# The player 1 is Kevin
Kev_str_count = 0

# counts the number of substring starting from a consonant
# The player 2 is Stuart
St_str_count = 0


for i in range(len(string)):
    if string[i].lower() in vowels.lower():
        Kev_str_count += (len(string)-i)
    else:
        St_str_count += (len(string)-i)

if Kev_str_count > St_str_count:
    print ("Kevin", kevsc)
elif Kev_str_count < St_str_count:
    print ("Stuart", St_str_count)
else:
    print ("Draw")