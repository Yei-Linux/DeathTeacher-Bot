from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, IntField

class pruebaBot(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathteacherbot?retryWrites=true&w=majority')['deathteacherbot']

    __schema__ = DictField(dict(
        text=StringField(required=False),
        search_text=StringField(required=False),
        conversation=StringField(required=False),
        persona=StringField(required=False),
        in_response_to=StringField(required=False),
        search_in_response_to=StringField(required=False),
        tags=StringField(required=False)
    ))
#statements.createIndex(Indexes.ascending("text"), indexOptions);
    #__indexes__ = [IndexModel("text", unique=False)]

