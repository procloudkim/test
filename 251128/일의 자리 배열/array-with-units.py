a, b = map(int, input().split())

arr = [a, b]          # 1항, 2항

for i in range(8):    # 이미 2개 있으니, 8개만 더 만들면 10개
    next_val = (arr[-2] + arr[-1]) % 10  # 전전항 + 전항의 일의 자리
    arr.append(next_val)

for x in arr:
    print(x, end=" ")
