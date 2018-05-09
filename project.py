from functions import *

opt = input('A: Wyświetl tekst \nB: Wyświetl teskt z podziałem z zdania \nC: Wyświetl tekst z podziałem na słowa \nD: Najczęściej występujące słowa w tekście \nCo chcesz zrobić:  ')

if opt == 'A':
    print(f)
elif opt == 'B':
    show_sent(text)
elif opt == 'C':
    show_word(text)
elif opt == 'D':
    count = int(input('\nJaki zakres pokazać? '))
    com_words(text, count)
else:
    print('Wprowadzono nieprawidłową wartość')
file.close()