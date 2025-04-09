import random
import math

def monte_carlo_circle(radius, num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if x ** 2 + y ** 2 <= radius ** 2:
            inside_circle += 1

    ratio = inside_circle / num_points
    area_square = (2 * radius) ** 2
    area_circle = ratio * area_square
    return area_circle


def monte_carlo_integral_sin(R, num_points):
    below_curve = 0

    for _ in range(num_points):
        x = random.uniform(0, R)
        y = random.uniform(0, math.sin(R))
        if y <= math.sin(x):
            below_curve += 1

    ratio = below_curve / num_points
    area_rectangle = R * math.sin(R)
    integral_value = ratio * area_rectangle
    return integral_value


def test_monte_carlo():
    radius = 1
    num_points_list = [100, 1000, 10000, 100000]
    exact_area_circle = math.pi * radius ** 2
    print("Dokładne pole koła:", exact_area_circle)

    for num_points in num_points_list:
        estimated_area_circle = monte_carlo_circle(radius, num_points)
        print(f"Szacowanie pola koła z {num_points} punktami: {estimated_area_circle}")

    print("\nCałka z sin(x) od 0 do R:")
    exact_integral_sin = 1 - math.cos(radius)
    print("Dokładna wartość całki:", exact_integral_sin)

    for num_points in num_points_list:
        estimated_integral_sin = monte_carlo_integral_sin(radius, num_points)
        print(f"Szacowanie całki z {num_points} punktami: {estimated_integral_sin}")


if __name__ == "__main__":
    test_monte_carlo()
