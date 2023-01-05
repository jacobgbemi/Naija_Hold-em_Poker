import os
import json

# with open('/etc/poker.json') as config_file:
# 	config = json.load(config_file)


class Config:
    """
    Object for key configurations
    """
    SECRET_KEY = "030cc42912626cb15434890ccf58db71" # os.environ.get('SECRET_KEY') 
    # SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" # os.environ.get('SQLALCHEMY_DATABASE_URI') 
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" # f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER: 'smtp.gmail.com'
    MAIL_PORT: 465
    MAIL_USE_TLS: False
    MAIL_USE_SSL: True
    MAIL_USERNAME: os.environ.get('EMAIL_USER') # config.get('EMAIL_USER')
    MAIL_PASSWORD: os.environ.get('EMAIL_PASSWORD') # config.get('EMAIL_PASSWORD')
