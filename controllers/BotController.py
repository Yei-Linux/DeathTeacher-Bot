from flask_restful import Resource,Api, reqparse
from webargs.flaskparser import use_args
from webargs import fields
from datetime import datetime
import config.chatterbot as chatterBotConfig
from helpers.SpeechHelper import SpeechHelper

class BotController(Resource):
    questionRequest = {
        "question": fields.String(required=True),
    }

    def __init__(self):
        self.speechHelper = SpeechHelper()

    @use_args(questionRequest)
    def post(self,request):
        print(request)
        answer = chatterBotConfig.bot.get_response(request['question'])
        return {"type":"message-row you-message","message": str(answer),"date":datetime.now().strftime("%H:%M:%S"),"bot":"bot1"}

