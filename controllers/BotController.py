from flask_restful import Resource,Api, reqparse
from webargs.flaskparser import use_args
from webargs import fields
from datetime import datetime
import config.chatterbot as chatterBotConfig
from helpers.SpeechHelper import SpeechHelper

class BotController(Resource):
    questionRequest = {
        "theme": fields.String(required=True),
    }

    def __init__(self):
        self.speechHelper = SpeechHelper()
   
    @use_args(questionRequest)
    def post(self,request):
        
        answer = chatterBotConfig.bot.get_response(request['question'])
        self.speechHelper.speakText(answer)
<<<<<<< HEAD
        return {"answer": str(answer)}

#a = BotController()
#b = {
#    "question": "hi"
#}
#c = a.post(b)

#print(c)
=======
        return {"type":"message-row you-message","message": str(answer),"date":datetime.now().strftime("%H:%M:%S"),"bot":"bot1"}
>>>>>>> christian
