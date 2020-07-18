from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, IntField

class User(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathteacherbot?retryWrites=true&w=majority')['deathteacherbot']

    __schema__ = DictField(dict(
        email=StringField(required=True),
        names=StringField(required=True),
        password=StringField(required=True),
        firstname=StringField(required=True),
        secondname=StringField(required=True)
    ))

    __indexes__ = [IndexModel('email', unique=True)]