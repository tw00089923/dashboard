from app import app

from flask import redirect, render_template, url_for, request, jsonify, flash, make_response, session, Response

import markdown

from app import api, login_manager

from flask_login import UserMixin, login_required, login_user, logout_user

from application.models import User, Task, Sensor

from flask_jwt import  current_identity, jwt_required
from collections import Counter
### this matplotly start
"""
@app.before_request
def user_login():
"""
    

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/",methods=["POST","GET"])
def login():
    error = {}
    username = ""
    if hasattr(session,"username")  :
        username = session["username"]
    if request.method == "POST":
        form = request.form
        #password = request.form["password"]
        user = User.query.filter_by(username=form["username"]).first()
        if not user :
            error = {'error':"使用者不存在"}
            return render_template("login.html",error=error,username=username)
        else :
            if not user.check_password(form["password"]):
                error= {'error':"密碼錯誤"}
                print(message)
            else:
                login_user(user, remember=True)
                return redirect("/dashboard")
        return render_template("login.html",username=username)
        print(user)
    return render_template("login.html",error=error,username=username)

@app.route("/api")
def api():    
    #print(os.path.exists(os.path.dirname(app.root_path+"/README.md")))
    with open(app.root_path + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route('/dashboard',methods=["POST","GET"])
@login_required
def dashboard():  

    tasks = Task.query.all()
    if request.method == "POST":
        print(Task.find_by_id(1).json())
        if tasks == None :
            tasks = ["錯誤"] 
    user = User.query.order_by(User.username).first()
    sensor = Sensor.query.all()
    time  = [ ids.time.strftime("%Y-%m-%d %H:%M:%S") for ids in sensor] 
    sensor_id = [ ids.sensor_id  for ids in sensor ]
    counter_sensor = Counter(sensor_id )
    return render_template(
        'layout.html',
        user=user , 
        tasks=tasks, 
        time=time, 
        sensor= sensor,
        sensor_id=list(counter_sensor.keys()),
        sensor_id_count = list(counter_sensor.values()) 
        )

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


@app.route('/protected',methods=["POST","GET"])
@jwt_required()
def protected():
    print("this protected is successed!!!")
    return '%s' % current_identity


'''
@app.route("/simple.png")
def simple():
    import datetime
    from io import BytesIO
    import random
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure(figsize=(5,5))

    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
'''