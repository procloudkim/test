count_3 = 0
count_5 = 0

for x in range(10):
    x = int(input())
    if x % 3 == 0:
        count_3 += 1
    if x % 5 ==0:
        count_5+= 1
print(count_3, count_5)