## Given the names and grades for each student in a class of N students, store them in a nested list 
## and print the name(s) of any student(s) having the second lowest grade.
## Also print the names alphabetically.

N = int(input())
nested_list = []
grade_list = []
for i in range(N):

    name = input().strip()
    grade = float(input())

    nested_list.append([name, grade])

def takefirst(element):
    return element[0]

nested_list.sort(key=takefirst)

for value in nested_list:
    grade_list.append(value[1])

mn = min(grade_list)
for value in nested_list:
    if value[1] == mn:
        grade_list.remove(mn)

for value in nested_list:
    if value[1] == min(grade_list):
        print(value[0])