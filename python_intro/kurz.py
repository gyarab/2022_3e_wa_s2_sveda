import httpx

row = ""
for r in httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt").text.split("\n"):
    if "|EUR|" in r:
        row = r.split("|")
        break

print(float(row[len(row) - 1].replace(",", ".")))

