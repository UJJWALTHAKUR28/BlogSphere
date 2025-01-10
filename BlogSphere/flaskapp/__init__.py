# to handle the import issues we will create package structure this structure the foleder will be created which will be same as file name with the project and it will be created th init file in the folder
import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager
from flask_mail import Mail
# cannot wrok we have circular import from models import User,Post
# Get the absolute path of the current file (flaskapp.py)
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "site.db")}'
db = SQLAlchemy(app)
#hasing of the password logics
Bcrypt1= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'
# app.config['MAIL_SERVER']='smtp.googlemail.com'
# app.config['MAIL_PORT']=587
# app.config['MAIL_USE_TLS']=True
# app.config['MAIL_USERNAME']
# app.config['MAIL_PASSWORD']
#mail=MAIL(app)
from flaskapp import routes
