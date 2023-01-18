import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
from resources.index_route import IndexRoute
from resources.user_route import UserRoute
from resources.middleware import Auth

load_dotenv()

app = Flask(__name__)

app.wsgi_app = Auth(app.wsgi_app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

api = Api(app, "/api")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return f'<User>: {self.email}>'

api.add_resource( IndexRoute, "/", methods=["GET"] )
api.add_resource( UserRoute, '/<int:user_id>/', methods=["GET"] )