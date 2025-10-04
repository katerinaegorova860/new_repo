from Address import Address
from Mailing import Mailing


to_address = Address("101000", "Москва", "Арбат", "12",)
from_address = Address("190000", "Санкт-Петербург", "Невский проспект", "5",)

mailing = Mailing(to_address, from_address, 350, "TRK123456789RU")

print(
    f"Отправление {mailing.track} из"
    f"{mailing.from_address.index}, {mailing.from_address.citi}, {mailing.from_address.street},"
    f"{mailing.from_address} - {mailing.from_address.apartment} "
    f"В {mailing.to_address.index}, {mailing.to_address.citi}, {mailing.to_address.street},"
    f"{mailing.to_address} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей"
)
