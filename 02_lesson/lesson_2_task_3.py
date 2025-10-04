import math


def square(side):
    area = side * side
    return math.ceil(area)


side = 4.3
result = square(side)


print(f"Сторона квадрата: {side}, площадь: {result}")
