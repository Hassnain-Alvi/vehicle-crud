import os

# third-party imports
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from flask_dotenv import DotEnv

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    env = DotEnv(app)
    from app import models
    from app.models import Cars

    app.app_context().push()
    db.init_app(app)
    db.create_all()

    # temporary route
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/list')
    def hello_world():
    	cars = Cars.query.all()
    	return render_template("list.html", cars=cars)
    
    return app