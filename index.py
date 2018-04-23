
ham = input('Wpisz liczby do sumowania oddzielając je spacją')  # pobiera input od użytkownika
spam = ham.split()   # rozdziela każdą liczbępo spacji
spam = [int(i) for i in spam] # spam jest listą, iterujemy po każdym jej elemencie i umieszczamy w liście jako int
i = sum(spam)   # sumuje spam
print(i)   # wyświetlamy sume

