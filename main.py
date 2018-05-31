import time
from functions import *
from nltk.tokenize import sent_tokenize
time.sleep(0.5)


opt = None
while opt != 'exit':
    file = open('melania.txt', 'r')
    f = file.read()
    text = sent_tokenize(f)

    opt = input("""\nDostępne opcje przetwarzania wczytanego tekstu:
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
        pass
# Wyświetla słowa niesklasyfikiwane
    elif opt == 'c':
        pass
# Możliwość dodania nowego słowa do leksykonu i określenia jego nacechowania
    elif opt == 'd':
        pass
# Sprawdza nacechowanie podanego słowa, jeśli jest dostępne w leksykonie
    elif opt == 'e':
        pass
# Kończy działanie programu
    elif opt == 'exit':
        print('Program zakończono.')
        break