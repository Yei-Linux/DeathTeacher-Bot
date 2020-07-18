from flask import Flask
from flask_restful import Resource,Api

from flask_cors import CORS
from controllers.BotController import BotController         
from controllers.DeepFakeController import DeepFakeController
from controllers.UserController import UserController

from controllers.FoodController import FoodController
import config.chatterbot as chatterBotConfig

app = Flask(__name__)
api = Api(app)

api.add_resource(BotController,'/death-teachers/bot')
api.add_resource(DeepFakeController,'/death-teachers/deep-fake')
api.add_resource(UserController,'/death-teachers/users')
api.add_resource(FoodController, '/death-teachers/food')
CORS(app)

if __name__ == "__main__":
    bot = chatterBotConfig.bot
    
    app.run(debug=True)
