A = int(input())                              # Number of elements in A
elements_of_A = set(map(int, input().split()))     # Space separated list of elements
N = int(input())                              # Number of other sets

def operations():
    if operation_name == 'update':
        elements_of_A.update(elements_of_other_set)

    elif operation_name == 'intersection_update':
        elements_of_A.intersection_update(elements_of_other_set)

    elif operation_name == 'difference_update':
        elements_of_A.difference_update(elements_of_other_set)

    else:
        elements_of_A.symmetric_difference_update(elements_of_other_set)

for i in range(N):
    operation_to_be_performed = input()
    operation_name = operation_to_be_performed.split()[0]
    length = int(operation_to_be_performed.split()[1])
    elements_of_other_set = set(map(int, input().split()))
    operations()

print(sum(elements_of_A))