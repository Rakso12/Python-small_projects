#Program z użyciem biblioteki SNAPS
#Wersja 1.1
#Autor: Oskar Tyniec
import pygame
import snaps
import time
snaps.display_image("background.jpg")
# Funkcja wyświetla tekst w kolorze 0,0,200 o rozmiarze 30 , usytuowany w lewo-horyzontalnie i na środek-vertykalnie
snaps.display_message("witaj w prostym programie",color=(255,255,255),size=40,horiz='right',vert='bottom')
time.sleep(3)
snaps.display_message("DING!")
snaps.play_sound("ding.wav")
time.sleep(3)