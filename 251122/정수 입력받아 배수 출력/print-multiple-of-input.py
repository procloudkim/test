N = int(input())

# 제한 조건 검사
if 1 <= N <= 100:
    for k in range(1, 6):   # 1,2,3,4,5
            print(N * k, end=" ")