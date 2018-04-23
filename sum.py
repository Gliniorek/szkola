ham = input('Wpisz liczby do sumowania')
spam = ham.split()
spam = [int(i) for i in spam] # spam jest listą, iterujemy po każdym jej elemencie i umieszczamy w liście jako int
i = sum(spam)
print(i)