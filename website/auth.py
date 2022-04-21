from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)  # Tworzenie blueprinta


@auth.route('/')  # poniższa funkcja odpali się, gdy wejdziemy w stonę [ROUTE_Z_BLUEPRINTA_W_APP/[ROUTE] w tym przypadku /auth/
def home():
    return "<h1>Test</h1>"


@auth.route('/login')
def login():
    return render_template("login.html", name='Dominik', boolean=False)


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
