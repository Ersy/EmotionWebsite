from app import app
from flask import render_template, request
import unirest
from forms import MessageForm
import database
from flask_navigation import Navigation
import emo_config_file # get API_KEY


# set the links for different pages
nav = Navigation(app)
nav.Bar('top', [
nav.Item('Home', 'index'),
nav.Item('Emotion App','emotion'),
nav.Item('Visualization','polynomial'),
nav.Item('DB','get_all_databases')
])

# home page
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

# emotion link page
@app.route('/emotion/')
def emotion():
	return render_template("my_form.html",mood='happy',form=MessageForm())

# send text to external API for sentiment analysis
@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
	  headers={
	    "X-Mashape-Key": EMO_API_KEY,
	    "Content-Type": "application/x-www-form-urlencoded",
    	"Accept": "application/json"
    	},
  		params={
    	"txt": msg
  		}
	)
	return render_template("my_form.html",mood=response.body['result']['sentiment'],form=MessageForm())



