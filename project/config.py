import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
#url for postgress database
#SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"
#url for sqlite dabatase
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "notes.db"))
SQLALCHEMY_DATABASE_URI = database_file
