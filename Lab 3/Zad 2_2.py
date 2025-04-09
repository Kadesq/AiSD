import Zad_2_1
from scipy.signal import square
from scipy.signal.windows import triang


def main():

    circle=Zad_2_1.Circle(5)
    triangle = Zad_2_1.Triangle(3, 4, 5)
    square = Zad_2_1.Square(4)

    print(f"Koło: pole = {circle.area()}, obwód = {circle.perimeter()}")
    print(f"Trójkąt: pole: {triangle.area()}, obwód = {triangle.perimeter()}")
    print(f"Kwadrat: pole: {square.area()}, obwód = {square.perimeter()}")

if __name__ == "__main__":
    main()