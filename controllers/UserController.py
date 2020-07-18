from flask_restful import Resource, reqparse
from webargs.flaskparser import use_args
from webargs import fields
from services.UserService import UserService

class UserController(Resource):
    userRequest = {
        "email": fields.String(required=True),
        "names": fields.String(required=True),
        "password": fields.String(required=True),
        "firstname": fields.String(required=True),
        "secondname": fields.String(required=True)
    }

    loginRequest = {
        "email": fields.String(required=True),
        "password": fields.String(required=True)
    }

    @use_args(userRequest)
    def post(self,request):
        UserService.insertUser(request)
        return {"message":"User inserted correctly"}

    @use_args(loginRequest)
    def put(self,request):
        exists = UserService.verifyUser(request)
        return {"isExists": exists}