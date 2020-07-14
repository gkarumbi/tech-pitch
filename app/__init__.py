from flask import flask
from flask_bootstrap import flask_bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #Creating app from congigurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)


    return app