from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, IntField, DateTimeField,ListField

class statements(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathteacherbot?retryWrites=true&w=majority')['deathteacherbot']

    __schema__ = DictField(dict(
        id=StringField(required=False),
        text=StringField(required=False),
        search_text=StringField(required=False),
        conversation=StringField(required=False),
        persona=StringField(required=False),
        in_response_to=StringField(required=False),
        search_in_response_to=StringField(required=False),
        created_at=DateTimeField(required=False),
        tags=ListField(required=False)
    ))
#statements.createIndex(Indexes.ascending("text"), indexOptions);
    #__indexes__ = [IndexModel("text", unique=False)]

