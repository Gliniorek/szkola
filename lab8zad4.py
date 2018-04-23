spam = input("Wpisz tekst: ")
spam = spam.split()
for ham in spam:
    if 't' in ham or 'T' in ham:
        print(ham)
