A, B = map(int, input().split())

total = 0

for x in range(A, B + 1):
    if x % 2 == 0:
        total += x
print(total)

