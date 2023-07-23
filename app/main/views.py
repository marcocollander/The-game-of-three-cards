from flask import render_template
from flask_login import current_user

from . import main
from .. import db
from ..models import User
from .forms import MainForm


@main.route("/", methods=["GET", "POST"])
def index():
    form = MainForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        user = User.query.filter_by(username="Marek").first()
        user_temp = User()
        user_temp.results = form.hit_percentage.data
        db.session.add(user_temp)
        db.session.commit()
        print(user)

    return render_template("index.html", form=form)
