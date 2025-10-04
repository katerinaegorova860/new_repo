def dev_by_three(number):
    if number % 3 == 0:
        return "Да"
    else:
        return "Нет"


num = 10


result = dev_by_three(num)


print(f"Делится ли на три {num} - {result}")
