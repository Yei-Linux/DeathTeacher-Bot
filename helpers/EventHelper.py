from datetime import datetime, timedelta


class EventHelper:
    @staticmethod
    def generateReleaseDate():
        releaseDate = datetime.now() + timedelta(7)
        return str(releaseDate.strftime("%Y-%m-%dT%H:%M:%S"))

    @staticmethod
    def generateUrlEvent(id):
        return 'http://localhost:3000/meet/'+id