from flask import Flask
from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_wtf.csrf import CSRFProtect
from config import config

moment = Moment()
csrf = CSRFProtect()


def create_app(config_name):

    config_name = 'development'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    csrf.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
