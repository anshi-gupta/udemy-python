# Write a function that returns the lesser of two different numbers if both numbers are even.
# but returns the greater if one or both are odd

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a<b:
            print('The lesser of two evens {} and {} is {}'.format(a, b, a))
        else:
            print('The lesser of two evens {} and {} is {}'.format(a, b, b))
    elif a%2 == 0 or b%2 == 0:
        if a>b:
            print('The greatest of {} and {} is {}'.format(a, b, a))
        else:
            print('The greatest of {} and {} is {}'.format(a, b, b))
    else:
         if a>b:
            print('The greatest of two odds {} and {} is {}'.format(a, b, a))
         else:
            print('The greatest of two odds {} and {} is {}'.format(a, b, b))

lesser_of_two_evens(2, 4)
lesser_of_two_evens(4, 2)
lesser_of_two_evens(3, 4)
lesser_of_two_evens(4, 3)
lesser_of_two_evens(7, 6)
lesser_of_two_evens(6, 7)
lesser_of_two_evens(3, 5)
lesser_of_two_evens(9, 7)
