import re
with open('zdania.txt', 'r') as f:
    tekst = f.read()
    ilosc = len(re.split(r'[.!?]+', tekst))
    tekst = tekst.split('. ')
    x = 0
    for line in tekst:
        print(line)
