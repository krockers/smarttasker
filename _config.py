import os

# grab folder
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'kukkost'

# define full path to DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
