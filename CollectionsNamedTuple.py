## Dr. John Wesley has a spreadsheet containing a list of student's ID, MARKS, CLASS and NAME.
## Your task is to help Dr. Wesley calculate the average marks of the students.

## INPUT FORMAT
## The first line contains an integer N, the total number of students.
## The second line contains the names of the columns in any order.
## The next  lines contains the ID, MARKS, CLASS and NAME under their respective column names.

## OUTPUT FORMAT
## Print the average marks of the list corrected to 2 decimal places.

from collections import namedtuple
N = int(input())
StudentInfo = namedtuple('StudentInfo', ' '.join(split for split in (input().strip().split())))
print("%.2f" % (sum(int(StudentInfo._make(input().strip().split()).MARKS) for _ in range(N))/N))





