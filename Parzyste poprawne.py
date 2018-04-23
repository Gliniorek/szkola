t = int(input("Wpisz liczbę testów"))
n = input("Wpisz liczby do testów oddzielając je spacją")
n = n.split(' ')
a, b, c, d = t, t, 0, 0
while b>0:
    print(n[0])
    if n[c%2==0] == 0:
        print("sdf")
        break

    b -= 1



'''
while int(b)>0:
    if int(n[a]) % 2 == 0: # parzyste
        print(n[a] + " parzysta")
    elif int(n[a]) == 2: #parzysta
        print(n[a] + " patrzysta")
    b -= 1
    a += 1
    spam -= 1
    continue
    '''