## Kevin and Stuart want to play the 'The Minion Game'.
    ## Game Rules
        ## Both players are given the same string, S.
        ## Both players have to make substrings using the letters of the string S.
        ## Stuart has to make words starting with consonants.
        ## Kevin has to make words starting with vowels.
        ## The game ends when both players have made all possible substrings.

        ## Scoring
        ## A player gets +1 point for each occurrence of the substring in the string S.

        ## For Example:
        ## String S= BANANA
        ## Kevin's vowel beginning word = ANA
        ## Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

s = "BANANA"
vowel = {}
cons = {}
i = 0

# For single letter count
for letter in s:
    if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        if letter not in vowel:
            vowel[letter] = 1
        else:
            vowel[letter] += 1
        i += 1
    else:
        if letter not in cons:
            cons[letter] = 1
        else:
            cons[letter] += 1
        i += 1

for k1, v1 in cons.items():
    print(k1, v1)
for k2, v2 in vowel.items():
    print(k2, v2)

