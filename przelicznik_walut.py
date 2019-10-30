import requests
import re

#podpięcie api nbp - kursy walut
r = requests.get('http://api.nbp.pl/api/exchangerates/tables/C').json()
r = r[0]
r = r['rates']

#kolorowanie kursów walut
colour_red = "\033[1;91m"
colour_green = "\033[1;32m"
end = "\033[0;0m"


#wypisanie kursów + dodanie do zmiennych wartości kursów
print("WALUTA/KUPNO/SPRZEDAŻ")
for currency in r:
    if (currency['code'] == "EUR"):
        print("EUR\t" + colour_green +"",  currency['bid'] ,""+ colour_red +"\t",currency['ask'],"" + end)
        eur_ask = currency['ask']
        eur_bid = currency['bid']
    if (currency['code'] == "USD"):
        print("USD\t" + colour_green +"",  currency['bid'] ,""+ colour_red +"\t",currency['ask'],"" + end)
        usd_ask = currency['ask']
        usd_bid = currency['bid']
    if (currency['code'] == "CAD"):
        print("CAD\t" + colour_green + "", currency['bid'], "" + colour_red + "\t", currency['ask'], "" + end)
        cad_ask = currency['ask']
        cad_bid = currency['bid']
    if (currency['code'] == "CHF"):
        print("CHF\t" + colour_green + "", currency['bid'], "" + colour_red + "\t", currency['ask'], "" + end)
        chf_ask = currency['ask']
        chf_bid = currency['bid']
    if (currency['code'] == "JPY"):
        print("JPY\t" + colour_green +"",  currency['bid'] ,""+ colour_red +"\t",currency['ask'],"" + end)
        jpy_ask = currency['ask']
        jpy_bid = currency['bid']
    if (currency['code'] == "CZK"):
        print("CZK\t" + colour_green +"",  currency['bid'] ,""+ colour_red +"\t",currency['ask'],"" + end)
        czk_ask = currency['ask']
        czk_bid = currency['ask']

print("Podaj kwotę do wymiany wraz z walutą:")
pobranie = input()

x = re.search('^(\d+(?:(?:\.|\,)\d{0,2})?){1}\s*([a-zA-Z]{3}){1}$', pobranie)
while(x == None):
    print("Prosze podaj kwotę wraz z walutą [pamiętaj o kropce zamiast przecinka oraz walucie i kwocie]")
    pobranie = input()
    x = re.search('^(\d+(?:(?:\.|\,)\d{0,2})?){1}\s*([a-zA-Z]{3}){1}$', pobranie)

kwota = float(x.group(1))
if x.group(2) == 'eur' or x.group(2) == 'EUR':
    print("Kwota w Euro =",eur_ask * kwota)
elif x.group(2) == 'usd' or x.group(2) == 'USD':
    print("Kwota w Dolarach =",usd_ask * kwota)
elif x.group(2) == 'cad' or x.group(2) == 'CAD':
    print("Kwota w Dolarach kanadyjskich =",cad_ask * kwota)
elif x.group(2) == 'chf' or x.group(2) == "CHF":
    print("Kwota we Frankach szwajcarskich =",chf_ask * kwota)
elif x.group(2) == 'jpy' or x.group(2) == 'JPY':
    print("Kwota w Jenach =",jpy_ask * kwota)
elif x.group(2) == 'czk' or  x.group(2) == 'CZK':
    print("Kwota w Koronach czeskich =",czk_ask * kwota)