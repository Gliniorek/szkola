import re
with open('zdania.txt', 'r') as f:
    text = f.read()
    count = len(re.split(r'[.!?]+', text))-1
    text = re.split(r'[.!?]+', text)
    x = 0
    sentence = text[x].split()

    while count!= x:
        for letter in sentence:
            if letter[0].isupper() == True:
                print(text[x])
        x += 1