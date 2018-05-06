f = open('zdania.txt', 'r')
zdanie = f.read()
print("Notatka ma", len(zdanie.split(".")) - 1, "zdań.")

f.close()