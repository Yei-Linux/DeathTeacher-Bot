from models.Events import Events

class EventService:
    @staticmethod
    def postEventOnMeetUp(event):
        eventInserted = Events.insert_one(event)
        return eventInserted
    @staticmethod
    def updateEvent(id,eventRequest):
        Events.update_one({'_id': id}, {'$set': eventRequest}, upsert=False)
