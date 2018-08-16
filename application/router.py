from app import app

from flask import redirect, render_template, url_for, request, jsonify, flash, make_response

import markdown

from app import api

from application.models import User, Task, Sensor
### this matplotly start

from collections import Counter

@app.route("/")
def index():    
    #print(os.path.exists(os.path.dirname(app.root_path+"/README.md")))
    with open(app.root_path + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)

@app.route('/dashboard',methods=["POST","GET"])
def dashboard():  
    if request.method == "POST":
        data = request.form
        print(data)
        if 'file' not in request.files:
            flash("File is not allowed")
            return redirect(request.url)
        file = request.files["file"]

    if request.method == "GET":
        tasks = Task.query.all()
        if tasks == None :
            tasks = ["錯誤"] 

    user = User.query.order_by(User.username).first_or_404()
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