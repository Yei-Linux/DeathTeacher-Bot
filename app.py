from flask import Flask
from flask_restful import Resource,Api

from flask_cors import CORS
from controllers.BotController import BotController
from controllers.DeepFakeController import DeepFakeController

import config.chatterbot as chatterBotConfig

app = Flask(__name__)
api = Api(app)

api.add_resource(BotController,'/death-teachers/bot')
api.add_resource(DeepFakeController,'/death-teachers/deep-fake')
CORS(app)

if __name__ == "__main__":
    bot = chatterBotConfig.bot
    #chatterBotConfig.trainningBot(bot)
    app.run(debug=True)
