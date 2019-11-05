import snaps
from datetime import datetime
from time import sleep

snaps.display_image("clock.jpg")
while True:
    time = datetime.now()
    snaps.display_message(time.strftime("%X"),color=(0,220,0),size=210)
    sleep(1)
