num = int(input("Liczba "))
if num == 2:
    print(num, "Tak")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "Nie")
            break
        else:
            print(num, "Tak")
            break
else:
    print(num, "Nie")
