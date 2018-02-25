DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO=True
DATABASE_CONNECT_OPTIONS = {}

API_KEY = "AIzaSyAg73PIqn1wjNUfixe-vF6sv9-7RjPqNd0"