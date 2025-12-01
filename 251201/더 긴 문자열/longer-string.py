w1, w2 = input().split()

len1 = len(w1)
len2 = len(w2)


if len1 == len2:
    print("same")
elif len1 > len2:
    print(w1, len1)
else:
    print(w2, len2)