from nltk.tokenize import sent_tokenize

file = open('melania.txt', 'r')
f = file.read()
text = sent_tokenize(f)

def show_text(argument):
    print(argument, '\n' * 2)

def show_sent(argument):  # dzieli tekst na zdania
    x = 1
    for sentence in argument:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(x, sentence)
            x += 1

    print('\n------------- Notes --------------------\n')

    for sentence in argument:
        if sentence[0].islower():
            print(sentence)

def show_word(argument):  # dzieli tekst na wyrazy
    sens = f.split()
    i = [i for i in sens]
    print(i[:10])


def count_words(argument):  # liczy ilość słów
    sens = f.split()
    z = 0
    for word in sens:
        z += 1
    print('Jest', z, 'słów w tym tekście')

def com_words(argument, count):  # liczy count(liczba) najczęściej pojawiających się słów
    import codecs
    import nltk

    default_stopwords = set(nltk.corpus.stopwords.words('english'))
    custom_stopwords = {'na', 'się', 'że', 'nie'}
    all_stopwords = default_stopwords | custom_stopwords
    fp = codecs.open('melania.txt', 'r', 'utf-8')

    words = nltk.word_tokenize(fp.read())
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if not word.isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in all_stopwords]

    fdist = nltk.FreqDist(words)
    print('\nNajczęściej występujące słowa:')
    for word, frequency in fdist.most_common(count):
        print(u'{}: {}'.format(word.title(), frequency))

def repl_word(argument1, argument2): #zmienia wybrane słowo na podane słowo
    import nltk
    text = nltk.sent_tokenize(f)
    text = [word.replace(argument1, argument2) for word in text]
    print(text, ' \n\n>>> Zmiany nie zostały zapisane <<<')

def len_words(argument): #pokazuje najdłuższe i nakrótsze słowo spełniające wymogi
    senstence = f.split()
    stop_words = {'na', 'sie', 'że', 'nie'}
    i = [word for word in senstence if len(word) > 2 and word not in stop_words]
    print('Wyłączająć \'stop words\':')
    print('Najdłuższe słowo w tekście to:', max(i,key=len))
    print('Najkrótsze słowo w tekście to:', min(i, key=len))