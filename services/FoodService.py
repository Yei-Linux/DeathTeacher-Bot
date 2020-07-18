import sys
sys.path.insert(0, "..")
from models.eatFood import statements
import json

class FoodService():
	@staticmethod
	def insertFood(food):
		statements.insert_one(food)


