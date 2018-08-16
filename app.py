from config import app_config

from flask_restful import Api

#from flask_bootstrap import Bootstrap

from flask import Flask
# Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. http://flask.pocoo.org/
from flask_sqlalchemy import SQLAlchemy
# 關連式資料庫 ORM http://flask-sqlalchemy.pocoo.org/2.3/
from flask_bcrypt import Bcrypt
# flask_bcrypt 密碼加密 http://flask-bcrypt.readthedocs.io/en/latest/ 
flask_bcrypt = Bcrypt()
# Flask(__name__ , template_folder='application/templates') 可頁面修改參數
app = Flask(__name__, template_folder='application/templates',static_url_path="/static")

#Bootstrap(app)

api = Api(app)

app.config.from_object(app_config["development"])

db = SQLAlchemy(app)

flask_bcrypt.init_app(app)



### import router ..... 
import  application.router

import application.api


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)