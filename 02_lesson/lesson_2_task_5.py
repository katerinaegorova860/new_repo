def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    if month in (3, 4, 5):
        return "Весна"
    if month in (6, 7, 8):
        return "Лето"
    if month in (9, 10, 11):
        return "Осень"
    else:
        return "Некорректный номер месяца"


print(month_to_season(2))  # Зима
print(month_to_season(7))  # Лето
print(month_to_season(11))  # Осень
print(month_to_season(15))  # Некорректный номер месяца
