n = int(input())

count = 0

for x in range(1, n + 1):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
        count += 1

print(count)
