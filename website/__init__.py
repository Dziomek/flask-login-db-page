from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'ABC'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # informacja dla app jak dotrzec do blueprintow
    app.register_blueprint(auth, url_prefix='/')

    return app