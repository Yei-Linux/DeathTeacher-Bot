from flask import request
from flask_restful import Resource, reqparse
import werkzeug
from io import BytesIO

from helpers.EventHelper import EventHelper
from helpers.GoogleCloudHelper import GoogleCloudHelper
from services.EventService import EventService

class EventController(Resource):
    def post(self):

            parse = reqparse.RequestParser()
            parse.add_argument('video', type=werkzeug.datastructures.FileStorage, location='files')
            args = parse.parse_args()

            data = request.get_json() or request.form
            data_to_insert = dict(
                title=data['title'],
                description=data['description'],
                urlImage=data['urlImage'],
                urlVideo=data['urlVideo'],
                urlEvent=data['urlEvent'],
                professor=data['professor'],
                releaseDate=data['urlVideo'],
                category=data['category']
            )

            videoBytes = args['video'].read()
            stream = BytesIO(videoBytes)

            gcp = GoogleCloudHelper()
            data_to_insert['releaseDate'] = EventHelper.generateReleaseDate()
            eventIdInserted = EventService.postEventOnMeetUp(data_to_insert)

            gcp.upload_blob(stream, str(eventIdInserted.inserted_id)+'_meet.mp4')
            urlVideo = gcp.getSignedUrlOfFile(str(eventIdInserted.inserted_id)+'_meet.mp4')
            urlEvent = EventHelper.generateUrlEvent(str(eventIdInserted.inserted_id))
            EventService.updateEvent(eventIdInserted.inserted_id,{'urlEvent': urlEvent, "urlVideo": urlVideo })

            return {"response" : urlVideo}
