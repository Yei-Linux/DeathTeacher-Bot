import sys
sys.path.insert(0, "..")
from models.Theme import Theme
import json

class ThemeService():
	@staticmethod
	def insertTheme(theme):
		Theme.insert_one(theme)


	@staticmethod
	def verifyTheme(theme):
		#print(theme)
		themeFound = Theme.find_one({'url': theme})
		#print("Found:",themeFound)
		if themeFound != None:
			return True
		return False