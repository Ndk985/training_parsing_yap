import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

pattern = re.compile(
    r'(?:город[а-яё]*\s+)(\w+).*?'      # город
    r'(?:улиц[а-яё]*\s+)(\w+).*?'       # улица
    r'(?:дом[а-яё]*\s+)(\d+).*?'        # дом
    r'(?:квартир[а-яё]*\s+)(\d+)',      # квартира
    re.IGNORECASE
)

for address in addresses:
    m = pattern.search(address)
    if m:
        city, street, house, apartment = m.groups()
        print(f"{city} {street} {house} {apartment}")
