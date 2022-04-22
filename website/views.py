from flask import Blueprint, render_template, request, flash
from .models import Note
from flask_login import login_user, login_required, logout_user, current_user
from . import db

# Blueprinty zawierają w sobie routy

views = Blueprint('views', __name__)  # Tworzenie blueprinta


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully', category='success')

    return render_template("home.html", user=current_user)

