#Gra większa - mniejsza (Zgadywanie liczby)
#Wersja 1.3
#Autor: Oskar Tyniec

import random
import time

print("Witaj w grze ZGADNIJ LICZBĘ!")
time.sleep(3)

#pobieramy liczbę od użytkownika oraz losujemy wzorzec liczby szukanej
print("Podaj liczbę:")
losowana_liczba = random.randint(1,100)
podana_liczba = int(input())
podejscia = int(1)

#sprawdzamy czy liczba jest odgadnięta poprawnie
while(podana_liczba != losowana_liczba):
    if(podana_liczba < losowana_liczba):
        print("Zbyt małą! Próbuj dalej")
    if(podana_liczba > losowana_liczba):
        print("Zbyt duża! Próbuj dalej!")
    podana_liczba = int(input())
    podejscia += 1

#wypisywanie wyniku i ilości podejść
print("TAK JEST! Liczba", podana_liczba, "to poprawna liczba")
print("Wybrałeś poprawną liczbę po :",podejscia,"próbach")