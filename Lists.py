## Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed
## above. Iterate through each command in order and perform the corresponding operation on your list.

N = int(input())
arr = []
for i in range(N):
    string = input()

    if 'print' not in string.split():

        if 'insert' in string.split():
            i = int(string.split()[1])
            e = int(string.split()[2])
            arr.insert(i, e)

        if 'remove' in string.split():
            e = int(string.split()[1])
            arr.remove(e)

        if 'append' in string.split():
            e = int(string.split()[1])
            arr.append(e)

        if 'sort' in string.split():
            arr.sort()

        if 'pop' in string.split():
            arr.pop()

        if 'reverse' in string.split():
            arr.reverse()

    else:
        print(arr)