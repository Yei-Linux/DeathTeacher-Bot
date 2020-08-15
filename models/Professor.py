from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, ListField, ObjectIDField

class Professors(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathMeetup?retryWrites=true&w=majority')['deathMeetup']

    __schema__ = DictField(dict(
        additionalInformation=ListField(required=False),
        fullName=StringField(required=True),
        urlImage=StringField(required=False),
        urlVideo=StringField(required=False),
        category=ObjectIDField(required=True),
        createdAt=StringField(required=True),
        deletedAt=StringField(required=False),
    ))