
from flask_restful import Resource, marshal_with, fields, reqparse, marshal

from app import api

from application.models import User, Task, CwbModel

import os

from flask_jwt import jwt_required, current_identity

###  Rest --- Api ---
 
# Look only in the POST body
# parser.add_argument('name', type=int, location='form')

# Look only in the querystring
# parser.add_argument('PageSize', type=int, location='args')

# From the request headers
# parser.add_argument('User-Agent', location='headers')

# From http cookies
# parser.add_argument('session_id', location='cookies')

# From file uploads
# parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')

auth_filed={
    "id": fields.Integer ,
    "username":fields.String ,
    "email": fields.String ,
    "password": fields.String ,
}

task_field={

    "id" : fields.Integer,
    "name" : fields.String,
    "classifer" : fields.String
}


class Register(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=str, required=True)
        parse.add_argument('email',type=str, required=True)
        parse.add_argument('password',type=str, required=True)
        args = parse.parse_args()
        user = User.query.filter_by(username=args["email"]).first()
        if user :
            return { "message" : "The email is exist" }, 201
        else:
            user = User(username=args["username"], email=args["password"], password=args["password"])
            user.save_to_db()
            return { "message" : "Create this account successfully" }, 200

class Auth(Resource):
    def get(self):
        # curl http://127.0.0.1:8080/api/v1/auth -d "username=auwit0205@gmail.com" -d "password=812323"
        parse = reqparse.RequestParser()
        parse.add_argument('username',type=str, required=True)
        parse.add_argument('password',type=str, required=True)
        args = parse.parse_args()
        user = User.query.filter_by(username=args["username"]).first()
        if user and user.check_password(args["password"]):
            return marshal(user,auth_filed)
        else :
            return None
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('email',type=str, required=True)
        parse.add_argument('password',type=str, required=True)
        args = parse.parse_args()
        user = User.query.filter_by(email=args["email"]).first()
        print(user)

        if user and user.check_password(args["password"]) :
            return { "success" : "true" }, 200
        elif user is None:
            return  { "type":"email", "message" : "The email is not exist " }, 201
        else:
            return  { "type":"password", "message" : "The password is wrong" }, 201
        #curl http://127.0.0.1:8080/api/v1/auth -d "task=something new" -d "email=auwit0205@gmail.com " "password=812323" -X POST -v 
        #curl -X GET http://localhost:8080/api/v1/board -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzQ2Njc0ODIsImlhdCI6MTUzNDY2NzE4MiwibmJmIjoxNTM0NjY3MTgyLCJpZGVudGl0eSI6MX0.-7cv141HOOytjUnjIKgR8FeBlqHerN-_3rBSSNUZrko"
class Post(Resource):
    #@jwt_required()
    def get(self): 
        task = Task.find_by_id(1).json()
        return marshal(task,task_field)
    @jwt_required()
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('name',type=str, required=True)
        parse.add_argument('classifer',type=str, required=True)
        args = parse.parse_args()
        task = Task(name=args["name"],classifer=args["classifer"])
        tasks = Task.query.all()
        try :
            task.save_to_db()  
            return {'success':"true"},201
        except : 
            return marshal( tasks,task_field), 403


cwb_field = {
    # locationName String
    # parameterName String
    # parameterValue String 
    # parameterUnit String 
    # startTime datetime
    # endTime datetime
    "id": fields.Integer,
    "locationName": fields.String,
    "elementName": fields.String,
    "startTime": fields.DateTime,
    "endTime": fields.DateTime,
    "parameterName": fields.String,
    "parameterValue": fields.String,
    "parameterUnit": fields.String,
}


class CwbHttp(Resource):
    '''
    # Wx 天氣現象
    # PoP 降雨機率 
    # CI 舒適度
    # MinT 最低溫度
    # MaxT 最高溫度
    '''
    def get(self,weathertype):
        Alltype = [ "Wx", "Pop", "CI", "MinT", "MaxT" ]
        if weathertype in Alltype :
            cwb = CwbModel.query.filter(CwbModel.elementName == weathertype).all()
            print(cwb)
            #return {"seccuss":"true"}, 200
            return marshal(cwb, cwb_field), 200

        else :
            return {"success":"false","result":"Query type is error"}

api.add_resource(Auth,'/api/v1/auth')
api.add_resource(Register,'/api/v1/auth/create')
api.add_resource(Post,'/api/v1/board')
api.add_resource(CwbHttp,'/api/v1/weather/<weathertype>')


'''

If you are using Flask-Restful like me, it is also possible this way:

api.add_resource(UserAPI, '/<userId>', '/<userId>/<username>', endpoint = 'user')
a then in your Resource class:

class UserAPI(Resource):

  def get(self, userId, username=None):
    pass

'''