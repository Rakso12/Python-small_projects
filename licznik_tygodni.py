import datetime

tydzien = datetime.datetime(2019,9,30)

print(tydzien.strftime("%W"))

tydzien_1 = datetime.datetime.now()
numer_tyg = tydzien_1.strftime("%W")
print(tydzien_1.strftime("%W"))
numer_tyg = int(numer_tyg)

if(numer_tyg % 2 == 0 ):
    print("Tydzień  - B")
else:
    print("Tydzień - A")