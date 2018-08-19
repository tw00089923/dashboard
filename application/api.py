
from flask_restful import Resource, marshal_with, fields, reqparse, marshal

from app import api

from application.models import User, Task

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

parse = reqparse.RequestParser()
parse.add_argument('username', type=str, required=True)
parse.add_argument('password',type=str, required=True)


class Auth(Resource):
    
    @marshal_with(auth_filed)
    def get(self):
        # curl http://127.0.0.1:8080/api/v1/auth
        user = User.query.order_by(User.id).all()[0]

        return User.query.order_by(User.id).all()
    @jwt_required
    def post(self):
        #json_data = request.get_json(force=True)
        #un = json_data["username"] 
        #pw = json_data["password"]
        #return jsonify(u=un,p=pw)
        args = parse.parse_args()
        # 尋找第一個符合的條件 
        user = User.query.filter_by(username=args["username"]).first()
        if user :
            print("OK")
            return {"message":"Email is exist"}, 201
        else:
            return {"message":"ok"}, 201
        # curl http://127.0.0.1:8080/api/v1/auth -d "task=something new" -d "email=auwit0205@gmail.com " "password=812323" -X POST -v 

    #curl -X GET http://localhost:8080/api/v1/board -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzQ2Njc0ODIsImlhdCI6MTUzNDY2NzE4MiwibmJmIjoxNTM0NjY3MTgyLCJpZGVudGl0eSI6MX0.-7cv141HOOytjUnjIKgR8FeBlqHerN-_3rBSSNUZrko"
class Post(Resource):
    @jwt_required()
    def get(self): 
        #print(current_identity)
        task = Task.find_by_id(1).json()
        return marshal(task,task_field)
    @jwt_required()
    def post(self):
        return {"message":"ok"}

api.add_resource(Auth,'/api/v1/auth')
api.add_resource(Post,'/api/v1/board')
