from io import BytesIO

from flask_restful import Resource, reqparse
import werkzeug
from deepFake.deepFake import DeepFake
from flask import request
from datetime import datetime

from helpers.GoogleCloudHelper import GoogleCloudHelper
from services.ProfessorService import ProfessorService


class DeepFakeController(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('video', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        data = request.get_json() or request.form
        data_to_insert = dict(
            additionalInformation=data['additionalInformation'],
            fullName=data['fullName'],
            urlImage='',
            urlVideo='',
            category=data['category'],
            createdAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            deletedAt=None
        )

        professorInserted = ProfessorService.postProfessorOnMeetUp(data_to_insert)

        imageBytes = args['image'].read()
        videoBytes = args['video'].read()
        stream = BytesIO(imageBytes)
        video_url = DeepFake.generateFakerVideo(imageBytes,videoBytes)
        image_url = DeepFakeController.upload_to_gcp(stream,str(professorInserted)+'.png')

        ProfessorService.updateEvent(professorInserted,{'urlImage': image_url, "urlVideo": video_url })

        return {"response" : image_url}

    @staticmethod
    def upload_to_gcp(buffer_file,file_name):
        gcp = GoogleCloudHelper()
        gcp.upload_blob(buffer_file,file_name)
        response = gcp.getSignedUrlOfFile(file_name)
        return response

