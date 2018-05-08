from nltk.tokenize import sent_tokenize
file = open('zdania.txt', 'r')
f  = file.read()
text = sent_tokenize(f)

for sentence in text:
    if sentence[0].isupper() and (('.' or '?' or '!') in sentence[-1]):
        print(sentence)
    elif sentence[-1] == '?':
        print(sentence)

print('\n------------- Notes --------------------\n')

for sentence in text:
    if sentence[0].islower():
        print(sentence)
file.close()