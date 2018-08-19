from config import app_config

from flask_restful import Api, Resource

#from flask_bootstrap import Bootstrap

from flask import Flask
# Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. http://flask.pocoo.org/
from flask_sqlalchemy import SQLAlchemy
# 關連式資料庫 ORM http://flask-sqlalchemy.pocoo.org/2.3/
from flask_bcrypt import Bcrypt
# flask_bcrypt 密碼加密 http://flask-bcrypt.readthedocs.io/en/latest/ 
from flask_login import LoginManager

from flask_jwt import JWT, jwt_required, current_identity


# Flask(__name__ , template_folder='application/templates') 可頁面修改參數
app = Flask(__name__, template_folder='application/templates',static_url_path="/static")

api = Api(app)

app.config.from_object(app_config["development"])

login_manager = LoginManager()

login_manager.init_app(app)

db = SQLAlchemy(app)

flask_bcrypt = Bcrypt()

flask_bcrypt.init_app(app)

from security import authenticate, identity



jwt = JWT(app, authenticate, identity)

# 查詢自身的JWT
#curl -H "Content-Type: application/json" -X POST -d '{"username":" ","password":" "}' http://localhost:8080/auth
#curl -X GET http://localhost:8080/protected -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzQ2NTU5NDYsImlhdCI6MTUzNDY1NTY0NiwibmJmIjoxNTM0NjU1NjQ2LCJpZGVudGl0eSI6MX0.tDOVv2_wyDglCem_fLG8HDSXZZ2X9S06wXPcrvWFGVA"


### import router ..... 
import application.router

import application.api


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)