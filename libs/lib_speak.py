import os
from gtts import gTTS
import temperature as tmp
from datetime import datetime
"""
La librairie speak_lib sert a convertir un texte en format audio
"""

def play(audio):
	try:
		os.system("sudo mpg321 -g 5 " + audio)
		return True
	except:
		return False


def say(text,path):
	speech = gTTS(text,lang='fr')
	speech.save(path)
	os.system("sudo mpg321 -g 20 " + path)

def say_time():
	hour = datetime.now().strftime('%H')
	minutes = datetime.now().strftime('%M')
	say("Il est actuellement {0} heures et {1} minutes".format(hour,minutes),"hour.mp3")
	os.system("sudo rm hour.mp3")

def say_temperature():
	temp,hum = tmp.get_temperature()
	say("Il fait actuellement {0} degrés et le taux d'humidité est de {1} pourcent".format(temp,hum),"temp.mp3")
	os.system("sudo rm temp.mp3")

def say_something(text):
        say(text,"sthg.mp3")
        os.system("sudo rm sthg.mp3")
