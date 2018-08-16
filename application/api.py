
from flask_restful import Resource, marshal_with, fields, reqparse

from app import api

from application.models import User

import os

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
parse = reqparse.RequestParser()
parse.add_argument('email', type=str, required=True)
parse.add_argument('password',type=str, required=True)


class Auth(Resource):
    @marshal_with(auth_filed)
    def get(self):
        # curl http://127.0.0.1:8080/api/v1/auth
        return User.query.order_by(User.id).all()
    def post(self):
        #json_data = request.get_json(force=True)
        #un = json_data["username"] 
        #pw = json_data["password"]
        #return jsonify(u=un,p=pw)
        args = parse.parse_args()
        # 尋找第一個符合的條件 
        user = User.query.filter_by(email=args["email"]).first()
        if user:
            print()
            print(user.check_password(args["password"]))
            return {"message":"Email is exist"}, 201
        else:
            return {"message":"ok"}, 401
        # curl http://127.0.0.1:8080/api/v1/auth -d "task=something new" -d "email= ,password=" -X POST -v 
class Post(Resource):
    def get(self):
        
        return {"love":"love"}



api.add_resource(Auth,'/api/v1/auth')
api.add_resource(Post,'/api/v1/board')
