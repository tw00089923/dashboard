from app import db, flask_bcrypt
from sqlalchemy.sql import expression

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(255))
    is_authenticated = db.Column(db.Boolean, default=False, server_default="true")
    is_active = db.Column(db.Boolean, default=False, server_default="true")
    is_anonymous = db.Column(db.Boolean, default=False, server_default="true")
    def __repr__(self):
        return "<User %r>"%self.username
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)
    def set_password(self, password):
        return flask_bcrypt.generate_password_hash(password)
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)
    def get_id(self):
        return self.id
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    classifer = db.Column(db.String(50))

    def __repr__(self):
        return "<User %r>"%self.name
    def __init__(self, name, classifer):
        self.name = name 
        self.classifer = classifer
    def json(self):
        return {
            "id":self.id,
            "name":self.name,
            "classifer":self.classifer
        }
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete_from_db(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

class Sensor(db.Model):
    __tablename__ = "sensor"
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float())
    humidity = db.Column(db.Float())
    time = db.Column(db.DateTime)
    sensor_id = db.Column(db.String(100))
    def __repr__(self):
        return "<Sensor %r>"%self.sersor_id
    def __init__(self, temperature, humidity  ,sensor_id, time ):
        self.temperature = temperature
        self.humidity =  humidity
        self.sensor_id = sensor_id
        self.time = time
class CwbModel(db.Model):
    '''
    Json 
    -locationName o
    -WeatherElement o
    --elementName o
    --time <list>
    ---startTime o
    ---endTime o
    ---parameter
    ----parameterName o
    ----parameterValue o

    # datasetDescription String 
    # locationName String
    # elementName String
    # parameterName String
    # parameterValue String 
    # parameterUnit String 
    # startTime datetime
    # endTime datetime

    # html http://opendata.cwb.gov.tw/opendatadoc/MFC/ForecastElement.pdf
    # Wx 天氣現象
    # PoP 降雨機率 
    # CI 舒適度
    # MinT 最低溫度
    # MaxT 最高溫度
    '''
    __tablename__ = "weather"
    id = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(db.String())
    elementName = db.Column(db.String())
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    parameterName  = db.Column(db.String())
    parameterValue  = db.Column(db.String())
    parameterUnit = db.Column(db.String())
    def __init__(self,locationName,elementName,startTime,endTime,parameterName,parameterUnit,parameterValue):
        self.locationName = locationName
        self.elementName = elementName
        self.startTime = startTime
        self.endTime = endTime
        self.parameterName = parameterName
        self.parameterValue = parameterValue
        self.parameterUnit = parameterUnit

    def __repr__(self):
        # return script 
        return "<CwbModel {0.locationName}>".format(self)
    def __str__(self):
        # print()
        return "{0.locationName} type : {0.elementName} : {0.startTime} ~ {0.endTime}, {0.parameterName}".format(self)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
#Integer	an integer
#String(size)	a string with a maximum length (optional in some databases, e.g. PostgreSQL)
#Text	some longer unicode text
#DateTime	date and time expressed as Python datetime object.
#Float	stores floating point values
#Boolean	stores a boolean value
#PickleType	stores a pickled Python object
#LargeBinary	stores large arbitrary binary data

'''
Simple Example => 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
## ont to Many =>

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')



class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)
## Many to Many => 

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

'''