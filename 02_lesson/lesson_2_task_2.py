def is_year_leap(year: int) -> bool:
    return year % 4 == 0


year = 2024
result = is_year_leap(year)


print(f"год {year}: {result}")
