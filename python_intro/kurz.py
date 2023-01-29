import httpx
from pick import pick
from time import sleep

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
data = httpx.get(URL).text.split("\n")
data = data[2:-1]
currencyJSON = {}
currencies = []
for row in data:
    row = row.split("|")
    currencyJSON.setdefault(row[3], float(row[4].replace(",", ".")) / int(row[2]))
    currencies.append(row[3])

currencyJSON.setdefault("CZK", 1)
currencies.append("CZK")
currencies.sort()


def calculate_currency():
    before_currency_input_title = "Vyberte vstupní měnu: "
    before_currency_input = pick(currencies, before_currency_input_title, "=>")
    print(before_currency_input_title + before_currency_input[0])

    after_currency_input_title = "Vyberte výstupní měnu: "
    after_currency_input = pick(currencies, after_currency_input_title, "=>")
    print(after_currency_input_title + after_currency_input[0])

    if before_currency_input == after_currency_input:
        print("Vstupní a výstupní měna nemůže být stejná! Zkuste to znovu...")
        sleep(2)
        return -1

    input_amount = input("Zadejte částku v " + before_currency_input[0] + ": ")

    if "," in input_amount:
        input_amount = input_amount.replace(",", ".")

    try:
        input_amount = float(input_amount)
    except ValueError:
        print("Částka musí být číslo! Zkuste to znovu...")
        sleep(2)
        return -1

    calculation_result = input_amount * currencyJSON.get(before_currency_input[0]) / currencyJSON.get(after_currency_input[0])

    return "Výsledek: " + str(calculation_result)


try_again = True
while try_again:
    result = calculate_currency()

    if result != -1:
        print(result)
        try_again = False
