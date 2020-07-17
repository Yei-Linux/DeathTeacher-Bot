import sys
sys.path.insert(0, "..")
from models.eatFood import pruebaBot
import json

class FoodService():
	@staticmethod
	def insertFood(food):
		pruebaBot.insert_one(food)


