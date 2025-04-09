import time
from turtledemo.penrose import start

from sympy.utilities.iterables import iterable


def loop_using_iterable():
    result = []
    iterable = [i for i in range(100000)]
    for item in iterable:
        result.append(item)
    return  result

def loop_using_range():
    result = []
    for i in range(100000):
        result.append(i)
    return  result

start_time = time.time()
result_iterable = loop_using_iterable()
end_time = time.time()

print(f"Czas wykonania petli 'for' na obiekcie iterowanym: {end_time - start_time:.6f} sekundy")

start_time = time.time()
result_range = loop_using_range()
end_time = time.time()

print(f"Czas wykonania petli 'for' w stylu C++: {end_time - start_time:.6f} sekundy")

if result_iterable == result_range:
    print("Obie petle zwrocily takie same wyniki.")
else:
    print("Wyniki petli roznia sie.")