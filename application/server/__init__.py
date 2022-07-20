from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='static')
api = Api(app)
app.config.from_pyfile('config.py')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# import routes
from application.server.modules.api import *