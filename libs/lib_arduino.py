# Import de la librairie serial
import serial
from collections import Counter
import time

# Ouverture du port serie avec :
# 115200 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0',timeout=1, baudrate=115200)

def get_uid():
	cpt = 0
	liste = []
	while cpt<10:
		uid = serialArduino.readline().decode("UTF-8")[:-2]
		liste.append(uid)
		cpt+=1
	mc = Counter(liste).most_common()
	serialArduino.flushOutput()
	if len(mc[0][0])==0:
		return None
	else:
		return mc[0][0]

print(get_uid())
