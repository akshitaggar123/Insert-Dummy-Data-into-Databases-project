import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/dummy_db"
