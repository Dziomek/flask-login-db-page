from flask import Blueprint

# Blueprinty zawierają w sobie routy
views = Blueprint('views', __name__)  # Tworzenie blueprinta


@views.route('/')
def print_sth():
    return "xddxdx"
