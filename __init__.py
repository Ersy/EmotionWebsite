from flask import Flask
import emo_config_file # get app secret key!

app = Flask(__name__)

app.secret_key = APP_SECRET_KEY

from app import views
import simple
import database

