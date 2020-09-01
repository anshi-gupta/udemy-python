# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of money only 
# if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(input())
sizes = list(map(int, input().strip().split()))
N = int(input())
total_money = 0
for _ in range(N):
    cust = input()
    size = int(cust.split()[0])
    money = int(cust.split()[1])
    if size in sizes:
        total_money += money
        i = sizes.index(size)
        sizes.pop(i)

print(total_money)


    
