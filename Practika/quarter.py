def quarter_of_year(month):
    if 1 <= month <= 3:
        return "1 квартал"
    elif 4 <= month <= 6:
        return "2 квартал"
    elif 7 <= month <= 9:
        return "3 квартал"
    elif 10 <= month <= 12:
        return "4 квартал"
    else:
        return "Некорректный номер месяца"

print(quarter_of_year(5))