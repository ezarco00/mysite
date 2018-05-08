from flask import Flask
from flask import render_template
import constants
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello from Emely'

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/register')
def register():
    return app.send_static_file('register.html')

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)
@app.route('/top_ten_songs')
def top_ten_songs():
    return render_template('top_ten_songs.html',
                            songs=constants.Top_Ten_Songs)
