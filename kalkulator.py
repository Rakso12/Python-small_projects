#Program ktory robi coś fajnego
#Wersja 1.0
#Autor - jakiś ludź

print("SUPER KALKULATOR !")

liczba_1 = float(input("Podaj liczbę "))

print('''
Podaj działanie
[1]  +
[2]  -
[3]  /
[4]  *
''')
dzialanie = int(input())

liczba_2 = float(input("Podaj druga liczbe"))

wynik = 0

if(dzialanie == 1):
    wynik = liczba_1 + liczba_2
elif(dzialanie == 2):
    wynik = liczba_1 - liczba_2
elif(dzialanie == 3 and liczba_2 != 0):
    wynik = liczba_1 / liczba_2
elif(dzialanie == 4):
    wynik = liczba_1 * liczba_2
else:
    print("no debil no")

print("Wynik to ",wynik)