from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphone 15", +79991234567),
    Smartphone("Samsung", "Galaxy 524", +79991234567),
    Smartphone("Xiaomi", "13 Pro", +79991234567),
    Smartphone("Google", "Pixel 8", "+79771234567"),
    Smartphone("Honor", "Magic6", "+79995554433")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone}")
