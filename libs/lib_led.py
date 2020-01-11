from grovepi import *
from driverI2C import *

RED_LED = 5
BLUE_LED = 6

pinMode(RED_LED, "OUTPUT")
pinMode(BLUE_LED, "OUTPUT")

def allumer(led):
	digitalWrite(led,1)
	pass

def eteindre(led):
	digitalWrite(led,0)
	pass

eteindre(RED_LED)
eteindre(BLUE_LED)
