import random
from collections import Counter

class Lotto:
    def __init__(self, liczby):
        if len(liczby) not in [5, 6]:
            raise ValueError("Lista musi zawierać 5 lub 6 liczb.")
        if not all (0<= x <= 48 for x in liczby):
            raise ValueError("Liczby muszą być z zakresu 0-48.")
        self.liczby = sorted(liczby)

    def sprawdz(self, inny_obiekt):
        return sorted(self.liczby) == sorted(inny_obiekt.liczby)

def graj (wybrane_liczby):
    lotto_obiekt = Lotto(wybrane_liczby)
    wylosowane = sorted(random.sample(range(49),6))
    trafione = set(lotto_obiekt.liczby).intersection(wylosowane)
    print(f"Twoje liczby: {lotto_obiekt.liczby}")
    print(f"wylosowane: {wylosowane}")
    print(f"Triafone: {trafione}")
    return len(trafione)

def analiza_losowan():
    zestawy = [tuple(sorted(random.sample(range(49), 6)))for _ in range(1000)]
    licznik = Counter()
    for zestaw in zestawy:
        licznik.update(zestawy)
    najczestsze = licznik.most_common()
    print("Najczęściej występujące liczby:")
    for liczba, ilosc in najczestsze[:10]:
        print((f"{liczba}: {ilosc} razy"))
    return najczestsze

def zapisz_do_pliku(lista, najczestsze):
    nazwa_pliku = f"{lista[0]}_{lista[1]}.txt"
    with open(nazwa_pliku, 'w') as f:
        f.write("Najczęściej występujące liczby:\n")
        for liczba, ilosc in najczestsze:
            f.write(f"{liczba}: {ilosc} razy\n")
        print(f"Wyniki zapisano w pliku: {nazwa_pliku}")

if __name__ == "__main__":
    moje_liczby = [5, 12, 23, 34, 41, 7]
    graj(moje_liczby)
    wyniki = analiza_losowan()
    zapisz_do_pliku(moje_liczby, wyniki)