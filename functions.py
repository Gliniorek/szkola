def search_for_text():
    import os, fnmatch, time
    list_of_files = os.listdir('.')
    pattern = '*.txt'
    print('Wyszukiwanie plików...')
    time.sleep(1.2)
    for entry in list_of_files:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)

def choose_text():
    choosen_text = input('Który z powyższych plików tekstowych chcesz wybrać? [nazwa.txt]')
    if choosen_text == 'positive-words.txt' or choosen_text == 'negative-words.txt':
        exit('Błąd dostępu. Program zakończono.')
    return str(choosen_text)

def show_text(argument):
    print(argument, '\n' * 2)

def show_sent(argument):  # dzieli tekst na zdania
    x = 1
    for sentence in argument:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(x, sentence)
            x += 1
def check_text_character():
    print('Opcja jeszce niedostępna')
    p = open('positive-words.txt', 'r')
    n = open('negative-words.txt', 'r')
    pos = p.read()
    neg = n.read()

# def show_word(argument):  # dzieli tekst na wyrazy
#     sens = f.split()
#     for word in sens:
#         print(word)
#
# def count_words(argument):  # liczy ilość słów
#     sens = f.split()
#     z = 0
#     for word in sens:
#         z += 1
#     print('Jest', z, 'słów w tym tekście')
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