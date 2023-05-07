year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 !=0:
        print("Високосный год")
    else:
        if year % 400 ==0:
            print("Високосный год")
        else:
            print("Не високосный")
else:
    print("Год не високосный")