sex = int(input()) # 0: man, 1: woman
age = int(input()) # 1~100



if age >=19:
    if sex == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    if sex == 0:
        print("BOY")
    else:
        print("GIRL")
    