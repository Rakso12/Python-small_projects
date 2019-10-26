#Przelicznik jednostek
#Wersja 1.0
#Autor: Oskar Tyniec
print("Witaj w programie przelicznik jednostek")
print("Wybierz jakie wielkości chcesz przeliczać")
print('''
[1] - temperatura
[2] - prędkość
[3] - waluty
''')
wybor_wielkosci = int(input())
if wybor_wielkosci==1:
    print("Przelicznik temperatury")
    print('''Wybierz system
    [1] - stopnie Celcjusza na stopnie Kelwina
    [2] - stopnie Kelwina na Celcjusza
    ''')
    przelicznik = int(input())
    print("Podaj jaką wartość chcesz zamienić")
    wartosc = float(input())
    if(przelicznik == 1):
        wynik = wartosc + 273.15
        print(wynik)
    if(przelicznik == 2):
        wynik = wartosc - 273.15
        print(wynik)
    else:
        print("Podałeś złe kryterium")
if wybor_wielkosci == 2:
    print("Przelicznik prędkości")
    print('''Wybierz system
    [1] - m/s na km/h
    [2] - km/h na m/s
    ''')
    przelicznik = int(input())
    print("Podaj wartość jaką chcesz zamienić")
    wartosc = float(input())
    if(przelicznik == 1):
        wynik = wartosc * 3.6
        print(wynik)
    if(przelicznik == 2):
        wynik = wartosc / 3.6
        print(wynik)
    else:
        print("Podałeś złe kryterium")