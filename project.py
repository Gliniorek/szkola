from functions import *
from nltk.tokenize import sent_tokenize
#some project scratch

opt = input('A: Wyświetl tekst\n'
            'B: Wyświetl teskt z podziałem z zdania\n'
            'C: Wyświetl tekst z podziałem na słowa\n'
            'C1: Polisz słowa w tekście\n'
            'D: Najczęściej występujące słowa w tekście\n'
            'E: Zamień słowo w tekście\n'
            'F: Pokaż najdłuższe i najkrótsze słowo w tekście'
            'Co chcesz zrobić:\n')
assert opt
if opt == 'A' or opt == 'a':
    print(f)
elif opt == 'B' or opt == 'b':
    show_sent(text)
elif opt == 'C' or opt == 'c':
    show_word(text)
elif opt == ' C1' or opt == 'c1':
    count_words(text)
elif opt == 'D' or opt == 'd':
    count = int(input('\nJaki zakres pokazać? '))
    com_words(text, count)
elif opt == 'E' or opt == 'e':
    argument1 = str(input('Jakie słowo chcesz zamienić?'))
    argument2 = str(input('Na jakie słowo chcesz zamienic?'))
    repl_word(argument1, argument2)
elif opt == 'F' or opt =='f':
    len_words(text)
else:
    print('Wprowadzono nieprawidłową wartość')
file.close()