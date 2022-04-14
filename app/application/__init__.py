from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from . import api

db = SQLAlchemy()
cors = CORS()

def init_app():
    app = Flask(__name__, instance_relative_config=False)#, instance_relative_config=False)

    app.config.from_object('config.Config')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)
    cors.init_app(app)

    #app.register_blueprint(api.Blueprint)


    with app.app_context():
        from . import routes

        db.drop_all()
        db.create_all()

        return app