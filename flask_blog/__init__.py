from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask (__name__)
app.config['SECRET_KEY'] = '9f6d9ff96124fbabf3e2fd84ee5d8869'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_mannager = LoginManager(app)
login_mannager.login_view = 'login'
login_mannager.login_message_category = 'info'

from flask_blog import route