y = int(input())

# if Y % 4 != 0:
#     print("false")
# else:
#     if Y % 100 == 0 and Y % 400 != 0:
#         print("false")
#     else:
#         print("true")  


if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("true")
else:
    print("false")