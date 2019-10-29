from datetime import datetime
from time import sleep
import os
import sys

if(sys.platform.startswith('linux')):
    clear = lambda: os.system('clear')
if(sys.platform.startswith('win32')):
    clear = lambda: os.system('cls')
else:
    print("coś nie tak")

while True:
    czas = datetime.now()
    print(czas.strftime("%X"))
    sleep(1)
    clear()
