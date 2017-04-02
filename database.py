from app import app
from flask_pymongo import PyMongo
from flask import jsonify
import os

# user and url for accessing DB
app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']

mongo = PyMongo(app)

# database page
@app.route('/database/collections', methods=['GET'])
def get_all_databases():
	return jsonify({'result': mongo.db.collection_names()})
