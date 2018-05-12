from functions import *
from nltk.tokenize import sent_tokenize

opt = input('A: Wyświetl tekst\n'
            'B: Wyświetl teskt z podziałem z zdania\n'
            'C: Wyświetl tekst z podziałem na słowa\n'
            'C1: Polisz słowa w tekście\n'
            'D: Najczęściej występujące słowa w tekście\n'
            'E: Zamień słowo w tekście\n'
            'Co chcesz zrobić:\n')
assert opt
if opt == 'A':
    print(f)
elif opt == 'B':
    show_sent(text)
elif opt == 'C':
    show_word(text)
elif opt == 'C1':
    count_words(text)
elif opt == 'D':
    count = int(input('\nJaki zakres pokazać? '))
    com_words(text, count)
elif opt == 'E':
    argument1 = str(input('Jakie słowo chcesz zamienić?'))
    argument2 = str(input('Na jakie słowo chcesz zamienic?'))
    repl_word(argument1, argument2)
else:
    print('Wprowadzono nieprawidłową wartość')
file.close()