import statistics
L=[1, 2]
for i in range (2, 48):
    next_value = (L[i-1]+L[i-2]) / (L[i-1] - L[i-2])
    L.append(next_value)

average = sum(L) / len(L)
median = statistics.median(L)
from collections import Counter
counts = Counter(L)
repeated_values = [key for key, value in counts.items() if value > 1]

print(f"Lista L: {L}")
print(f"Średnia: {average}")
print(f"Mediana: {median}")
if repeated_values:
    print(f"Wartości, które pojawiły się więcej niż raz: {repeated_values}")
else:
    print("Brak wartości, które pojawiły się więcej niż raz.")
