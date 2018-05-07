import re
with open('zdania.txt', 'r') as f:
    text = f.read()
    count = len(re.split(r'[.!?]+', text))-1
    text = re.split(r'[.!?]+', text)
    x = 0
    while count>0:
        if text[x].islower():
            x += 1
            count -= 1
            continue
        else:
            print(text[x])
            count -= 1
            x += 1