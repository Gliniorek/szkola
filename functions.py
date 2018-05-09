from nltk.tokenize import sent_tokenize
file = open('melania.txt', 'r', encoding='UTF-8')
f  = file.read()
text = sent_tokenize(f)

def show_sent(argument): # dzieli tekst na zdania
    x = 1
    for sentence in argument:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(x, sentence)
            x += 1

    print('\n------------- Notes --------------------\n')

    for sentence in argument:
        if sentence[0].islower():
            print(sentence)

def show_word(argument): # dzieli tekst na wyrazy
    sens = f.split()
    for word in sens:
        print(word)

def com_words(argument, count): # liczy 10 najczęściej pojawiających się słów
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