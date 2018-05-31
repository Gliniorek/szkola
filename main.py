from functions import *
from nltk.tokenize import sent_tokenize

opt = None
choosen_text = ''

if choosen_text == '':
    search_for_text()
    file = open(choose_text(), 'r', encoding='UTF-8')
    f = file.read()
    text = sent_tokenize(f)
else:
    file = open(str(choose_text()), 'r')
    f = file.read()
    text = sent_tokenize(f)

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
        check_text_character(text)
# Wyświetla słowa niesklasyfikiwane
    elif opt == 'c':
        print('Opcja jeszce niedostępna')
# Możliwość dodania nowego słowa do leksykonu i określenia jego nacechowania
    elif opt == 'd':
        print('Opcja jeszce niedostępna')
# Sprawdza nacechowanie podanego słowa, jeśli jest dostępne w leksykonie
    elif opt == 'e':
        print('Opcja jeszce niedostępna')
# Kończy działanie programu
    elif opt == 'exit':
        print('Program zakończono.')
        break
    file.close()

