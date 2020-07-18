from flask_restful import Resource, reqparse
from webargs.flaskparser import use_args
from webargs import fields
import sys
sys.path.insert(0, "..")
from services.FoodService import FoodService
from datetime import datetime, tzinfo, timedelta

import collections
from webargs.flaskparser import use_args
from webargs import fields
from helpers.foodHelper import foodHelper


from flask import Flask, request

class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

class WiqipediaController(Resource):

    classRequest = {
        "topic": fields.String(required=True)
    }

    @use_args(classRequest)
    def post(self, request):
    	#react
        
        theme_dict= foodHelper().getContentTheme(request['topic'])
        
        food_dict = collections.defaultdict(dict)
        
        i=0
        for key in theme_dict:
            
            food_dict[str(i)]["id"] = ""
            food_dict[str(i)]["text"] = "que es" + key +"?"
            food_dict[str(i)]["search_text"] = ""
            food_dict[str(i)]["conversation"] =  "training"
            food_dict[str(i)]["persona"] =  ""
            
            food_dict[str(i)]["in_response_to"] = theme_dict[key]
            food_dict[str(i)]["search_in_response_to"] =  theme_dict[key]
            food_dict[str(i)]["created_at"] = datetime.utcnow().replace(tzinfo=simple_utc()).isoformat()
            food_dict[str(i)]["tags"] = [theme_dict[key]]
            i = i+1
        
        i=0
        for i in range(0, len(theme_dict)):
            
            FoodService.insertFood(food_dict[str(i)])
        return {"response":theme_dict}