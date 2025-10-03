from math import ceil

def min_boxes(items):
    return ceil(items / 5)


things = int(input("Введите количество предметов: "))


print(f"Для {things} предметов нужно {min_boxes(things)} коробок")