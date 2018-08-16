from app import db, flask_bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(255))
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