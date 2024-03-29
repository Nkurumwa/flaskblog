from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config_options

db =SQLAlchemy()
bcrypt = Bcrypt()
login_manager =LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_name):
  app =  Flask (__name__)
  app.config.from_object(config_options[config_name])

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)

  from .request import configure_request
  configure_request(app)

  from flaskblog.users.routes import users
  from flaskblog.posts.routes import posts
  from flaskblog.main.routes import main
#   from flaskblog.errors.handlers import errors
  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)
#   app.register_blueprint(errors)

  return app