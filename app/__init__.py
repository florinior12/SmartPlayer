#Import Flask
from flask import Flask

#Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#Create the app object
app = Flask(__name__)
#Load configurations from config file
app.config.from_object('config')
db = SQLAlchemy(app)
app.secret_key = app.config['SECRET_KEY']

from app import routes
print(app.config['SQLALCHEMY_DATABASE_URI'])


