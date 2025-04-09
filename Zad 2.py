import time
import  statistics

from array import array
from statistics import median

from Demos.SystemParametersInfo import new_value
from PIL.DdsImagePlugin import item1


def generate_array_with_time():
    L = array('d', [1,2])

    for i in range(2, 48):
        new_value = (L[i-1] + L[i-2]) / (L[i-1] - L[i-2])
        L.append(new_value)

    mean = statistics.mean(L)
    median = statistics.median(L)

    duplicates = {}

    for num in L:
        if L.count(num) > 1:
            duplicates[num] = L.count(num)

    if duplicates:
        print("Wartosci, ktore pojawily sie wiecej niz raz: ")
        for value, count in duplicates,items():
            print(f"Wartosc {value} pojawila sie {count} razy")
        else:
            print("Brak wartosci, ktore pojawily sie wiecej niz raz.")

    print(f"Srednia: {mean}")
    print(f"Mediana: {median}")

def generate_list_with_time():
    L1 = [1, 2]

    for i in range(2, 48):
        new_value = (L1[i-1] + L1[i-2]) / (L1[i-1] - L1[i-2])
        L1.append(new_value)

    mean = statistics.mean(L1)
    median = statistics.median(L1)

    duplicates = {}

    for num in L1:
        if L1.count(num) > 1:
            duplicates[num] = L1.count(num)

    if duplicates:
        print("Wartosci, ktore pojawily sie wiecej niz raz: ")
        for value, count in duplicates,items():
            print(f"Wartosc {value} pojawila sie {count} razy")
        else:
            print("Brak wartosci, ktore pojawily sie wiecej niz raz.")

    print(f"Srednia: {mean}")
    print(f"Mediana: {median}")


start_time = time.time()
generate_array_with_time()
end_time= time.time()
print(f"Czas wykonania z tablica: {end_time - start_time:.6f} sekundy")

start_time=time.time()
generate_list_with_time()
end_time = time.time()
print(f"Czas wykonania z lista: {end_time - start_time:.6f} sekundy")