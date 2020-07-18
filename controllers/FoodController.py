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
class FoodController(Resource):

    classRequest = {
        "topic": fields.String(required=True)
    }
    
    @use_args(classRequest)
    def post(self, request):
        list_food = foodHelper().getFood(request['topic'])
        for i in range(0, len(list_food)):
        	print(list_food[str(i)])
        	FoodService.insertFood(list_food[str(i)])
        return {"message":"food inserted correctly"}

    
  




