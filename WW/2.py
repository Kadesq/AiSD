from collections import Counter

class Cztytelnik:
    def __init__(self):
        self.tekst = []
        self.plik = None

    def OTWORZ(self, nazwa_pliku):
        try:
            self.plik = open(nazwa_pliku, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Nie znaleziono pliku.")
            self.plik = None

    def CZYTAM(self):
        if self.plik:
            linie = self.plik.readlines()
            self.tekst = [linie[i].strip() for i in range(0, len(linie), 2)]
        else:
            print("Plik nie został otwarty.")

    def SZUKAM(self, ciag_znakowy):
        return any(ciag_znakowy in linia for linia in self.tekst)

    def LICZ(self, litera):
        licznik = sum(linia.lower().count(litera.lower()) for linia in self.tekst)
        return licznik

    def ZAMYKAM(self):
        if self.plik:
            self.plik.close()
            self.plik = None

def znajdz_najczestsza_litere(nazwa_pliku):
    czyt = Cztytelnik()
    czyt.OTWORZ(nazwa_pliku)
    czyt.CZYTAM()

    caly_tekst = ''.join(czyt.tekst).lower()

    litery = [znak for znak in caly_tekst if znak.isalpha()]
    licznik = Counter(litery)

    if licznik:
        najczestsza, ile = licznik.most_common(1)[0]
        print(f"Najczęściej występująca litera to: '{najczestsza}' ({ile} razy)")
    else:
        print("Brak liter do analizy.")

    czyt.ZAMYKAM()
