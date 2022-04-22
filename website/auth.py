from flask import Blueprint, render_template, request, flash, redirect, url_for

from . import db
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)  # Tworzenie blueprinta


@auth.route('/')
def home():
    return "<h1>Test</h1>"


@auth.route('/login', methods=['GET', 'POST'])  # aby dekorator obsługiwał żądania GET i POST
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Invalid credentials. Try again', category='error')
        else:
            flash('User does not exist.', category='error')
    return render_template("login.html")  # name='Dominik', boolean=False)


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('User with this email already exists.')
        elif len(email) < 4:
            flash('Email length must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name length must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Successfully registered', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
