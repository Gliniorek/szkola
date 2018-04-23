ham = input("Wpisz tekst")
spam = ham.lower()

if spam.count('a') > spam.count('e'):
    print("W tekście <<", ham, ">> znajduje się więcej liter 'a' niż liter 'e'.")
elif spam.count('e') > spam.count('a'):
    print("W tekście <<", ham, ">> znajduje się więcej liter 'e' niż liter 'a'.")
elif spam.count('e') == spam.count('a') and (spam.count('a') or spam.count('e')) > 0:
    print("W tekście <<", ham, ">> znajduje się tyle samo liter 'e' jak liter 'a'.")
else:
    print("W tekście <<", ham, ">> nie ma żadnej litery 'a' lub 'b")