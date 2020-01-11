# Import de la librairie serial
import serial
from collections import Counter
import time
import threading

# Ouverture du port serie avec :
# 115200 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0',timeout=1, baudrate=115200)
lock = threading.RLock()


def get_uid2():
	cpt = 0
	liste = []
	while cpt<10:
		uid = serialArduino.readline().decode("UTF-8")[:-2]
		print(uid)
		liste.append(uid)
		cpt+=1
	mc = Counter(liste).most_common()
	serialArduino.flushOutput()
	if len(mc[0][0])==0:
		return None
	else:
		return mc[0][0]



def get_uid():
	serialArduino.flushOutput()
	uid = ""
	attempt = 0
	lock.acquire()
	while len(uid)<10 and attempt<10:
		uid = serialArduino.readline().decode("UTF-8")[:-2]
		attempt += 1
	
	lock.release()
	if len(uid)<10:
		return None
	else:
		return uid


