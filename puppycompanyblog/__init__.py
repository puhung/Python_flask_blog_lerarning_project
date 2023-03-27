# hold all the organization logic: connecting blueprint, connecting login manager
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
##################################
## DATABASE SETUP#################
##################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##################################
## LOGIN CONFIGS #################
##################################
login_manager = LoginManager()

login_manager.init_app(app) # pass app into login_manager
login_manager.login_view = 'users.login' # tell user which view function to go to when they need to log in.

from puppycompanyblog.core.views import core # import core blueprint
from puppycompanyblog.error_pages.handlers import error_pages
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages) # this blue print will link the viewsto our app
app.register_blueprint(users)
app.register_blueprint(blog_posts)