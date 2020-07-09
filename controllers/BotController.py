from flask_restful import Resource,Api, reqparse
from webargs.flaskparser import use_args
from webargs import fields

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
        answer = chatterBotConfig.bot.get_response(request['question'])
        self.speechHelper.speakText(answer)
        return {"answer": str(answer)}