# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not return False.

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        print(True)
    else:
        print(False)

makes_twenty(12, 8)      # T
makes_twenty(20, 3)      # T
makes_twenty(3, 20)      # T
makes_twenty(20, 20)     # T
makes_twenty(12, 15)     # F
