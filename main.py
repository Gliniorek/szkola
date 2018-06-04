from functions import *
from nltk.tokenize import sent_tokenize

opt = None
choosen_text = ''

if choosen_text == '':
    file = open(str(search_for_text()), 'r', encoding='UTF-8')
    f = file.read()
    file_text = f.split()
    text = sent_tokenize(f)
else:
    exit('Niespodziewany błąd podczas wczytywania pliku tekstowego.')

while opt != 'exit':
    opt = input(f"""\nDostępne opcje przetwarzania wczytanego tekstu [{file.name}]:
                A: Wyświetl tekst.
                B: Charakter tekstu (pozytywny/negatywny/neutralny).
                C: Wyświetl słowa niesklasyfikowane pod względem nacechowania.
                D: Dodaj słowo do leksykonu.
                E: Sprawdź nacechowanie podanego słowa.
                Powiedz co chcesz zrobić? \n
                 Wpisz exit aby zakończyć działanie programu""")
    print('\n')
    opt = opt.lower()

# Pokazuje cały tekst z oryginalnym formatowaniem
    if opt == 'a':
        show_text(f)
        opt = input('Czy chcesz wyświetlić tekst z podziałem na zdania? [T/N]')
        opt = opt.lower()
        if opt == 't':
            show_sent(text)
            continue

# Sprawdza tekst i pokazuje czy jest poz., neg. w procentach i % słów neutralnych oraz ilość słów niesklasyfikowanych
    elif opt == 'b':
        print(f'Słowa pozytywne to: {check_positives(file_text)}')
        print(f'Słowa negatywne to: {check_negatives(file_text)}')
        print(f'Jest {count_nochar(file_text)} niesklasyfikowanych.')
        z = count_words(file_text)
        x = (count_positives(file_text) / z) * 100
        y = (count_negatives(file_text) / z) * 100
        print(f'Słowa pozytywne stanowią {round(x, 2)}% tekstu, natomiast słowa negatywne to {round(y,2)}% tekstu.' )
# Wyświetla słowa niesklasyfikiwane
    elif opt == 'c':
        print(r'10 pierwszych wyrazów, które się są sklasyfikowane w leksykowanach:')
        print(f'Jest {count_nochar(file_text)} niesklasyfikowanych.')

# Możliwość dodania nowego słowa do leksykonu i określenia jego nacechowania
    elif opt == 'd':
        print('Opcja jeszce niedostępna')

# Sprawdza nacechowanie podanego słowa, jeśli jest dostępne w leksykonie
    elif opt == 'e':
        word = input('Wpisz słowo, którego charakter chcesz sprawdzić:')
        print(show_char(str(word)))
# Kończy działanie programu
    elif opt == 'exit':
        print('Program zakończono.')
        break

file.close()

