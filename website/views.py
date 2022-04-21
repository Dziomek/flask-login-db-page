from flask import Blueprint, render_template

# Blueprinty zawierają w sobie routy
views = Blueprint('views', __name__)  # Tworzenie blueprinta


@views.route('/')
def print_sth():
    return render_template("home.html")

