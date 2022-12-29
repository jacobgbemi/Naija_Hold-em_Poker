import os
import json

with open('/etc/poker.json') as config_file:
	config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER: 'smtp.gmail.com'
    MAIL_PORT: 465
    MAIL_USE_TLS: False
    MAIL_USE_SSL: True
    MAIL_USERNAME: config.get('EMAIL_USER')
    MAIL_PASSWORD: config.get('EMAIL_PASSWORD')
