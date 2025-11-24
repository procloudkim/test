N, M = map(int, input().split())

# Please write your code here.

# while 2<= N <= M <= 1000000:
#     print("현재 값:", N)
#     N=N%M

while N > 0 :
    print(N)
    N = N // M

