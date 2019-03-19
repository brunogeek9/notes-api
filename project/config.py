import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
#url for postgress database
#SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"
#url for sqlite dabatase
SQLALCHEMY_DATABASE_URI = "sqlite:///notes.db"
