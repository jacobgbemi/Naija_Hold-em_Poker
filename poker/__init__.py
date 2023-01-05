from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from poker.config import Config
import os


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    """
    Setup for application factory.
    Ensuring multiple instances of the application running at the same time
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # if app.config['LOG_WITH_GUNICORN']:
    #     gunicorn_error_logger = logging.getLogger('gunicorn.error')
    #     app.logger.handlers.extend(gunicorn_error_logger.handlers)
    #     app.logger.setLevel(logging.DEBUG)
    # else:
    #     file_handler = RotatingFileHandler('instance/flask-user-management.log',
    #                                        maxBytes=16384,
    #                                        backupCount=20)
    #     file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
    #     file_handler.setFormatter(file_formatter)
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)

    # # Remove the default logger configured by Flask
    # app.logger.removeHandler(default_handler)

    # app.logger.info('Starting the Flask User Management App...')


    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    from poker.users.routes import users
    from poker.posts.routes import posts
    from poker.main.routes import main
    from poker.game.routes import games
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(games)
    

    return app