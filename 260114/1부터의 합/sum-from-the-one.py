n = int(input())

total = 0

for x in range(1, 101):
    total += x
    if total >= n:
       print(x)
       break