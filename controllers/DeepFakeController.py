from flask_restful import Resource, reqparse
import werkzeug
from deepFake.deepFake import DeepFake

class DeepFakeController(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('video', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        imageBytes = args['image'].read()
        videoBytes = args['video'].read()

        response = DeepFake.generateFakerVideo(imageBytes,videoBytes)
        return {"response" : response}

