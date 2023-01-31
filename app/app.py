from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.secrets import db_access_uri
db = SQLAlchemy()


def create_app():
    app = Flask("__name__")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_access_uri
    app.config['SQLALCHEMY_TRACK_MODIDFICATIONS'] = False

    db.init_app(app)

    from app.models.Author import Author
    from app.models.Book import Book

    with app.app_context():
        db.create_all()

    from app.routes import bp
    app.register_blueprint(bp)

    return app


