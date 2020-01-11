import sys
sys.path.insert(0, '/home/pi/Projet/routineconfig')
sys.path.insert(1, '/home/pi/Projet/libs')

from app import Web
import lib_arduino
from api.manager import Manager
import tasks
import threading
import time
from core.execution import ExecutionThread


class ByCardActivator(threading.Thread):

	def __init__(self, manager):
		threading.Thread.__init__(self, daemon=True)
		self.manager = manager

	def run(self):
		old = None
		counter = 0
		while True:
			card_id = lib_arduino.get_uid()

			if card_id is None:
				old=None
				continue

			counter = 0
			card = self.manager.find_card_by_id(card_id)

			if card is not None and card.id != old:
				routine = self.manager.find_routine(card.routine_name)
				if routine is not None:
					old = card.id
					ExecutionThread(routine).start()
			


manager = Manager()
manager.register_task(tasks.LedTask())
manager.register_task(tasks.TemperatureTask())
manager.register_task(tasks.WaitTask())
manager.register_task(tasks.ExecuteAt())
manager.register_task(tasks.SaySomething())
manager.register_task(tasks.SayTime())

ByCardActivator(manager).start()

web = Web(manager, lib_arduino.get_uid)
application = web.app
