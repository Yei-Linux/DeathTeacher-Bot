from _datetime import datetime, timedelta


class EventHelper:
    @staticmethod
    def generateReleaseDate():
        return str(datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))

    @staticmethod
    def generateUrlEvent(id):
        return 'http://localhost:3000/meet/'+id