from api.task import Task
import lib_led
import lib_speak
import api.arg_type as arg
import time

class LedTask(Task):

	def __init__(self):
		Task.__init__(self, "Allumer ou Eteindre une LED")
		self.register_argument("Couleur", arg.choice("Rouge", "Bleue"))
		self.register_argument("Action", arg.choice("Allumer", "Eteindre"))

	def execute_task(self, arg_values):
		led = lib_led.RED_LED if arg_values["Couleur"] == "Rouge" else lib_led.BLUE_LED
		if arg_values["Action"] == "Allumer":
			lib_led.allumer(led)
		else:
			lib_led.eteindre(led)


class TemperatureTask(Task):

	def __init__(self):
		Task.__init__(self, "Dire la température et humidité")


	def execute_task(self, arg_values):
		lib_speak.say_temperature()


class WaitTask(Task):
	
	def __init__(self):
		Task.__init__(self,"Attendre (durée)")
		self.register_argument("Heures", arg.integer(minimum=0,maximum=23))
		self.register_argument("Minutes", arg.integer(minimum=0,maximum=59))
		self.register_argument("Secondes", arg.integer(minimum=0, maximum=59))

	def execute_task(self, arg_values):
		temps = int(arg_values["Heures"]) * 3600 + int(arg_values["Minutes"]) * 60 + int(arg_values["Secondes"])
		time.sleep(temps)


class ExecuteAt(Task):
	
	def __init__(self):
		Task.__init__(self, "Attendre (heure précise)")
		self.register_argument("Heures", arg.integer(minimum=0, maximum=23))
		self.register_argument("Minutes", arg.integer(minimum=0, maximum=59))

	def execute_task(self, arg_values):
		while time.localtime().tm_hour != int(arg_values["Heures"]) or time.localtime().tm_min != int(arg_values["Minutes"]):
			time.sleep(55)

class SaySomething(Task):

	def __init__(self):
		Task.__init__(self,"Dire quelque chose")
		self.register_argument("Phrase", arg.string(max_length=50))
		
	def execute_task(self,arg_values):
		lib_speak.say_something(arg_values["Phrase"])

class SayTime(Task):

	def __init__(self):
                Task.__init__(self,"Dire l'heure")

	def execute_task(self,arg_values):
		lib_speak.say_time()
