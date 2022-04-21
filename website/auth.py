from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)  # Tworzenie blueprinta


@auth.route('/')
def home():
    return "<h1>Test</h1>"


@auth.route('/login', methods=['GET', 'POST']) # aby dekorator obsługiwał żądania GET i POST
def login():
   return render_template("login.html") #name='Dominik', boolean=False)


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email length must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name length must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Successfully registered', category='success')

    return render_template("sign_up.html")
