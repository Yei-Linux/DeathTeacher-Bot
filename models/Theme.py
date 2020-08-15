from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, IntField, DateTimeField,ListField

class Theme(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathteacherbot?retryWrites=true&w=majority')['deathteacherbot']

    __schema__ = DictField(dict(
        url=StringField(required=False),
        content=StringField(required=False)
    ))

