from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from website import models

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.secret_key = 'ABC'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) # łączenie bazy danych z aplikacją

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')  # informacja dla app jak dotrzec do blueprintow
    app.register_blueprint(auth, url_prefix='/')

    import website.models   # alternatywnie: import .models as models

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database')

