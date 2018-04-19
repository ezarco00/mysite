from flask import Flask
from flask import render_template
import constants

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Emely'

@app.route('/about_me')
def about_me():
    return app.send_static_file('about_me.html')

#@app.route('/class_schedule')
#def class_schedule():
    #return app.send_static_file('class_schedule.html')

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)