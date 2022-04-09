from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import api


db = SQLAlchemy()

def init_app():
    app = Flask(__name__ )#, instance_relative_config=False)

    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)

    #app.register_blueprint(api.Blueprint)


    with app.app_context():
        from . import routes

        db.create_all()

        return app