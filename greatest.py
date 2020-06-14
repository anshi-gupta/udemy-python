### Write a function that returns the lesser of two numbers if both numbers are even, 
### but returns greater if one or both numbers are odd

def number(a,b):
    if a%2 == 0 and b%2 == 0:
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
            
print(number(10,13))
