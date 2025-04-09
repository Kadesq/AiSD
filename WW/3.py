import random
import statistics

class Analizator:
    def __init__(self):
        self.liczby = [random.randint(0, 100) for _ in range(500)]

    def MINIMALNY(self):
        return min(self.liczby)

    def MAKSYMALNY(self):
        return max(self.liczby)

    def SUMUJE(self):
        return sum(self.liczby)

    def ODCHYL(self):
        return statistics.stdev(self.liczby)

    def MSU(self):
        try:
            return statistics.mode(self.liczby)
        except statistics.StatisticsError:
            return "Brak jednoznacznej mody"

    def MDU(self):
        return statistics.median(self.liczby)

    def ZAPISUJE(self):
        nazwa_pliku = f"{self.liczby[0]}.txt"
        with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
            plik.write("Lista 500 losowych liczb:\n")
            plik.write(', '.join(map(str, self.liczby)) + "\n\n")

            plik.write(f"Najmniejsze element: {self.MINIMALNY()}\n")
            plik.write(f"Największy element: {self.MAKSYMALNY()}\n")
            plik.write(f"Suma: {self.SUMUJE()}\n")
            plik.write(f"Odchylenie standardowe: {self.ODCHYL():.2f}\n")
            plik.write(f"Moda: {self.MSU()}\n")
            plik.write(f"Mediana: {self.MDU()}\n")

obiekt = Analizator()
obiekt.ZAPISUJE()
