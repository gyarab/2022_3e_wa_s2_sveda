from time import sleep

import httpx
from pick import pick
from termcolor import colored

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
data = httpx.get(URL).text.split("\n")
data = data[2:-1]
currency_json = {}
for row in data:
    row = row.split("|")
    if row[3] > "CZK":
        currency_json.setdefault("CZK", 1)

    currency_json.setdefault(row[3], float(row[4].replace(",", ".")) / int(row[2]))


def calculate_currency():
    before_currency_input_title = "Vyberte vstupní měnu: "
    before_currency_input = pick(list(currency_json.keys()), before_currency_input_title, "=>")
    print(colored(before_currency_input_title, 'yellow') + colored(before_currency_input[0], "magenta"))

    after_currency_input_title = "Vyberte výstupní měnu: "
    after_currency_input = pick(list(currency_json.keys()), after_currency_input_title, "=>")
    print(colored(after_currency_input_title, 'yellow') + colored(after_currency_input[0], "magenta"))

    if before_currency_input == after_currency_input:
        print(colored("Vstupní a výstupní měna nemůže být stejná! Zkuste to znovu...", "red"))
        sleep(2)
        return -1

    input_amount = input(colored("Zadejte částku v " + before_currency_input[0] + ": ", "yellow"))

    if "," in input_amount:
        input_amount = input_amount.replace(",", ".")

    try:
        input_amount = float(input_amount)
    except ValueError:
        print(colored("Částka musí být číslo! Zkuste to znovu...", "red"))
        sleep(2)
        return -1

    calculation_result = input_amount * currency_json.get(before_currency_input[0]) / currency_json.get(
        after_currency_input[0])

    return "Výsledek: " + str(calculation_result)


try_again = True
while try_again:
    result = calculate_currency()

    if result != -1:
        print(colored(result, "green"))
        try_again = False
