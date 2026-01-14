n = int(input())

for grade in range(n, 101):

    if grade >= 90:
        print("A", end=" ")
    elif grade >= 80:
        print("B", end=" ")
    elif grade >= 70:
        print("C", end=" ")
    elif grade >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")

