from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
#flask_sqlalchemy is an ORM For Databases
from flask_migrate import Migrate
#flask_migrate is to manage migration of files


app = Flask(__name__, instance_relative_config=True) # our flask app
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)  
from app import models
