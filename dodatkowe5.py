
from nltk.tokenize import sent_tokenize
file = open('zdania.txt', 'r')
f  = file.read()
text = sent_tokenize(f)

def check_text(argument):
    for sentence in text:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(sentence)

    print('\n------------- Notes --------------------\n')

    for sentence in text:
        if sentence[0].islower():
            print(sentence)

check_text(text)
file.close()