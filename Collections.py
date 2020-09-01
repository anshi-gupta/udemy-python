# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only 
# if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

from collections import Counter
x = int(input())
sizes = Counter(list(map(int, input().strip().split())))
n = int(input())
total_money = 0
for _ in range(n):
    cust = input()
    size = int(cust.split()[0])
    money = int(cust.split()[1])
    if sizes[size]:
        total_money += money
        sizes[size] -= 1

print(total_money)

    
