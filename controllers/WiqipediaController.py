from flask_restful import Resource, reqparse
from webargs.flaskparser import use_args
from webargs import fields
import sys
sys.path.insert(0, "..")
from services.FoodService import FoodService
from services.ThemeService import ThemeService

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
        
        getContentTheme= foodHelper().getContentTheme(request['topic'])
        theme_dict = getContentTheme[0]
        theme_url = getContentTheme[1]

        if ThemeService.verifyTheme(theme_url) == True:
           print("tema buscado")
           return {"response":theme_dict}
        else:
            
            print("tema nuevo")
            food_dict = collections.defaultdict(dict)
            lista_key = ["url", "content"]
            lista_value=[theme_url, theme_dict]
            dictionary_theme = dict(zip(lista_key, lista_value))
            #prueba = {'url': 'https://es.wikipedia.org/wiki/Matem%C3%A1ticas', 'content': 'hola'}
            #print(type(dictionary_theme))
            #print(dictionary_theme)
            ThemeService.insertTheme(dictionary_theme)

            #ThemeService.insertTheme(theme_dict)
            i=0
            for key in theme_dict:
                food_dict[str(i)]["id"] = ""
                food_dict[str(i)]["text"] = theme_dict[key]
                food_dict[str(i)]["search_text"] = ""
                food_dict[str(i)]["conversation"] =  "training"
                food_dict[str(i)]["persona"] =  ""
                
                food_dict[str(i)]["in_response_to"] = "que es" + key +"?"
                food_dict[str(i)]["search_in_response_to"] = "que es" + key +"?"
                food_dict[str(i)]["created_at"] = datetime.utcnow().replace(tzinfo=simple_utc()).isoformat()
                food_dict[str(i)]["tags"] = [theme_dict[key]]
                i = i+1
            
            i=0
            for i in range(0, len(theme_dict)):
                #print(type(food_dict[str(i)]))
                #print(food_dict[str(i)])
                FoodService.insertFood(food_dict[str(i)])
            return {"response":theme_dict}



       