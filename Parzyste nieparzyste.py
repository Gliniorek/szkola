spam = input("Wpisz zdanie:")
for ham in spam.split():
    if len(ham) == 3:
        if ham[0].isupper():
            print(ham)