n = int(input())

nums = list(map(int, input().split()))

for i in range(n):
    squared= nums[i] * nums[i]

    print(squared,end=" ")