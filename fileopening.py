import re
f = open('melania.txt', 'r')
tekst = f.read()
tekst = " ".join(re.split("\s+", tekst, flags=re.UNICODE))
tekst = tekst.strip()
tekst = tekst.replace('. ', '\n')
print(tekst)
f.close()