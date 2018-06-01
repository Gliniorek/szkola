# Wyszukiwuje pliki tekstowe w aktualnym katalogu
def search_for_text():
    import os, fnmatch, time
    print('Wykryto powyższe teksty w katalogu:')
    time.sleep(0.5)
    listOfFiles = os.listdir('.')
    pattern = "*.txt"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
    choosen_text = input('Który z tych tekstów chcesz wczytać?')
    return str(choosen_text)

# Wybieranie pliku tekstowego do dalszej obróbki
def choose_text():
    choosen_text = input('Który z powyższych plików tekstowych chcesz wybrać? [nazwa.txt] \n')
    if choosen_text == 'positive-words.txt' or choosen_text == 'negative-words.txt':
        exit('Błąd dostępu. Program zakończono.')
    return str(choosen_text)


# Wyświetla wczytany tekst z oryginalnym formatowaniem
def show_text(argument):
    print(argument, '\n' * 2)

# Dzieli wczytany tekst na zdania i je numeruje
def show_sent(argument):
    x = 1
    for sentence in argument:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(x, sentence)
            x += 1

# Kolejne 4 funkcje sprawdzają jakie są negatywne i pozytywne słowa
# Oraz sprawdzają ich ilość
def check_positives(argument):
    l_file = open(r'positive-words.txt', 'r', encoding='UTF-8')
    f = l_file.read()
    lex = f.split()
    i = [i for i in argument if i in lex]
    i = list(set(i))
    return i

def check_negatives(argument):
    l_file = open(r'negative-words.txt', 'r', encoding='UTF-8')
    f = l_file.read()
    lex = f.split()
    i = [i for i in argument if i in lex]
    i = list(set(i))
    return i

def count_positives(argument):
    j = 0
    for spam in argument:
        if spam in check_positives(argument):
            j += 1
    print(f'Razem jest {j} pozytywnych słów.')

def count_negatives(argument):
    j = 0
    for spam in argument:
        if spam in check_negatives(argument):
            j += 1
    print(f'Razem jest {j} negatywnych słów.')

# Liczy ilość słów niesklasyfikowanych w leksykonach
def count_nochar(argument):
    j = 0
    i = 0
    for spam in argument:
        if spam in check_positives(argument):
            j += 1
    for spam in argument:
        if spam in check_negatives(argument):
            i += 1
    x = i + j
    return x

# def show_word(argument):  # dzieli tekst na wyrazy
#     sens = f.split()
#     for word in sens:
#         print(word)
#
def count_words(argument):  # liczy ilość słów
    sens = f.split()
    z = 0
    for word in sens:
        z += 1
    print('Jest', z, 'słów w tym tekście')
#
# def com_words(argument, count):  # liczy count(liczba) najczęściej pojawiających się słów
#     import codecs
#     import nltk
#
#     default_stopwords = set(nltk.corpus.stopwords.words('english'))
#     custom_stopwords = {'na', 'się', 'że', 'nie'}
#     all_stopwords = default_stopwords | custom_stopwords
#     fp = codecs.open('melania.txt', 'r', 'utf-8')
#
#     words = nltk.word_tokenize(fp.read())
#     words = [word for word in words if len(word) > 1]
#     words = [word for word in words if not word.isnumeric()]
#     words = [word.lower() for word in words]
#     words = [word for word in words if word not in all_stopwords]
#
#     fdist = nltk.FreqDist(words)
#     print('\nNajczęściej występujące słowa:')
#     for word, frequency in fdist.most_common(count):
#         print(u'{}: {}'.format(word.title(), frequency))
#
# def repl_word(argument1, argument2): #zmienia wybrane słowo na podane słowo
#     import nltk
#     text = nltk.sent_tokenize(f)
#     text = [word.replace(argument1, argument2) for word in text]
#     print(text, ' \n\n>>> Zmiany nie zostały zapisane <<<')
#
# def len_words(argument): #pokazuje najdłuższe i nakrótsze słowo spełniające wymogi
#     senstence = f.split()
#     stop_words = {'na', 'sie', 'że', 'nie'}
#     i = [word for word in senstence if len(word) > 2 and word not in stop_words]
#     print('Wyłączająć \'stop words\':')
#     print('Najdłuższe słowo w tekście to:', max(i,key=len))
#     print('Najkrótsze słowo w tekście to:', min(i, key=len))