import requests
r = requests.get('http://api.nbp.pl/api/exchangerates/tables/C').json()

r = r[0]
print(r)

r = r['rates']

print("WALUTA - KUPNO - SPRZEDAŻ")
for currency in r:
    if currency['code'] == "EUR":
        print("EUR\t", currency['bid'],"\t",currency['ask'])
