from PIL.ImImagePlugin import number
from werkzeug.http import parse_if_range_header

lista = []

for i in range(500,3001):
    if i%7==0 and i%5!=0:
        lista.append(i)

ciag_znakowy = "".join(str(number) for number in lista)
print(ciag_znakowy)

liczba_wystapien = ciag_znakowy.count('21')

ciag_znakowy_nowy = ciag_znakowy.replace('21', 'XX')

print()
print(ciag_znakowy_nowy)
print(liczba_wystapien)