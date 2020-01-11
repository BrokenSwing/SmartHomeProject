import temperature as tmp
import lib_speak as speak
import time

for i in range (0,2):
	i = tmp.get_temperature()
	speak.play("/home/pi/Projet/libs/start.mp3")
