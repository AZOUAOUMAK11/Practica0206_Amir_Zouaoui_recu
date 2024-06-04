import urllib.request
link = 'http://textfiles.com/adventure/aencounter.txt'
file = (urllib.request.urlopen(link))
print(file)

palabras = file.read()

cuenta_palabras = palabras.split()
print(len(cuenta_palabras))