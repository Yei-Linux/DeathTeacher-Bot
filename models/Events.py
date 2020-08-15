from pymongo import MongoClient, IndexModel
from pymongoext import Model, DictField, StringField, IntField, ObjectIDField

class Events(Model):
    @classmethod
    def db(cls):
        return MongoClient('mongodb+srv://123:123@cluster0-j3ras.mongodb.net/deathMeetup?retryWrites=true&w=majority')['deathMeetup']

    __schema__ = DictField(dict(
        title=StringField(required=True),
        description=StringField(required=True),
        urlImage=StringField(required=False),
        urlVideo=StringField(required=False),
        urlEvent=StringField(required=False),
        category=ObjectIDField(required=True),
        professor=ObjectIDField(required=True),
        releaseDate=StringField(required=True),
        createdAt=StringField(required=True),
        deletedAt=StringField(required=False),
    ))