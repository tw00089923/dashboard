import os 

from flask_script import Manager
# writing external scripts https://flask-script.readthedocs.io/en/latest/
from flask_migrate import Migrate, MigrateCommand
# 
from app import db, app

from application.models import User, Task, Sensor



app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db',MigrateCommand)

@manager.option('-n', '--config', dest='config', default='development')
def run(config):
    app.run(host="0.0.0.0",port=8080)

@manager.command
def create_table():
    db.create_all()
    # db.create_all(bind=['users']) single 
@manager.command
def drop_table():
    db.drop_all()
@manager.command
def insert_db():
    me = User(
        username = "admin",
        email = "auwit0205@gmail.com",
        password = "812323"
    )
    if User.query.filter_by(email=me.email).first() and User.query.filter_by(username=me.username).first():
        print("Database is exist")
        db.session.add(me)
        db.session.commit()
  
    task = Task(name = "富邦",classifer = "理財")
    db.session.add(task)
    db.session.commit()
    db.session.close()

@manager.command
def insert_db_all():
    import datetime , random
    sensor_board = [ 'Attin85' , 'Arduino Uno' , 'Raspberrypi 3 A', 'Raspberrypi 3 B']

    for i in range(100):
        sensor = Sensor(
        temperature = round(random.uniform(24,36),2),
        humidity  = round(random.uniform(0,1),2),
        time = datetime.datetime(2012,1,10)+datetime.timedelta(days=i),
        sensor_id = random.choice(sensor_board))
        db.session.add(sensor)
        db.session.commit()
    db.session.close()

@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-u', '--url', dest='url', default=None)
def check(name,url):
    print("{} , {} ".format(name,url))

if __name__ == '__main__':
    manager.run()

