from flask_restful import Resource, reqparse
from webargs.flaskparser import use_args
from webargs import fields
import sys
sys.path.insert(0, "..")
from services.FoodService import FoodService


import collections
from webargs.flaskparser import use_args
from webargs import fields
from helpers import foodHelper


from flask import Flask, request


class FoodController(Resource):
	themerequest = {
        "theme": fields.String(required=True)
    }

    @use_args(themerequest)
    def post(self, request):
        list_food = helpers.foodHelper().getFood(request)
        for i in range(0, len(list_fsood)):
        	print(list_food[str(i)])
        	FoodService.insertFood(list_food[str(i)])
        return {"message":"food inserted correctly"}

    
    def postWiki(self, request):
    	#react
        theme_dict= helpers.foodHelper().getContentTheme(request)
        food_dict = collections.defaultdict(dict)
        i=0
        for key in theme_dict:
            food_dict[str(i)]['text'] = "que es" + key +"?"
            food_dict[str(i)]['in_response_to'] = theme_dict[key]
            i = i+1
        print(food_dict)
        i=0
        for i in range(0, len(theme_dict)):
            print(food_dict[str(i)])
            FoodService.insertFood(food_dict[str(i)])
        return {"message":"lesson inserted correctly"}


