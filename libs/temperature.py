import grovepi
import math
import datetime


pin = 4
def get_data(i):
	if (i<50):
		try:
			[temp,humidity] = grovepi.dht(pin,0)
			if math.isnan(temp) == False and math.isnan(humidity) == False:
				if temp != 0 and humidity != 0:
					#Good data
					return [temp,humidity]
				else:
					#[0,0]
					print("Error reading")
					return get_data(i+1)
			else:
				#[nan,nan]
				print("Error reading")
				return get_data(i+1)
		except:
			#Can't read
			print("Error")
			return [-1,-1]

def get_temperature():
	tempHum = [0,0]
	cpt = 0
	#Get 20 measures to be more precise
	for i in range(0,20):
		stamp = get_data(0)
		if stamp != [-1,-1]:
			cpt += 1
			tempHum[0] += stamp[0]
			tempHum[1] += stamp[1]
	if cpt > 0:
		#Make the average
		tempHum[0] = tempHum[0]/cpt
		tempHum[1] = tempHum[1]/cpt
		#Insert the values
		return tempHum
	else:
		return None
		print("Sensor issue")


