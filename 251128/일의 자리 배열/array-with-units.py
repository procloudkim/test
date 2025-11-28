a, b = map(int, input().split())

arr = [a, b]          # 1항, 2항

for i in range( ??? ):      # 몇 번 더 만들어야 하지?
    next_val = ???          # 전전항 + 전항의 일의 자리
    arr.append(next_val)

# 여기서 arr에는 10개가 들어있어야 함
for x in arr:
    print(x, end=" ")
