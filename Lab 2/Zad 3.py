import time

txt = str(input("Podaj tekst: "))
split = txt.split()

print()

if len(split) == 1:
    print(f"Podano jeden wyraz: {txt}")
    print(f"Małymi literami: {txt.lower()}")

    start = time.time()

    f = open('SJP.txt', 'r', encoding='utf-8')
    txt1 = f.read()
    print('------')

    if txt.lower() in txt1:
        print("Jest w słowniku.")
    else:
        print("Nie ma w słowniku.")
    f.close()

    koniec = time.time()

    print(f"Czas przetwarzania: {koniec-start} sekund.")
else:
    print(f"Za dużo słów. ({split})")
    quit()