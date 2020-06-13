# Given an integer, returns True if n is within 10 of either 100 or 200

def almost_there(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10:
        print(True)
    else:
        print(False)

almost_there(90)              # T
almost_there(104)             # T
almost_there(150)             # F
almost_there(209)             # T