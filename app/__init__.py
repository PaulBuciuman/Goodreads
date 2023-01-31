from .app import create_app

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.controller.db_ingestion import bp
# db = SQLAlchemy()
#
#
# def create_app():
#     from app.models.Author import Author
#     app = Flask("__name__")
#     app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:admin@localhost:5432/postgres'
#     app.config['SQLALCHEMY_TRACK_MODIDFICATIONS'] = False
#
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#
#     app.register_blueprint(bp)
#
#     return app
#
#
# app = create_app()
#
#
# @app.route("/")
# def hello():
#     return 'helloooo'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
