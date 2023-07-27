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
       current_user.change_results(form.hit_percentage.data)

    return render_template("index.html", form=form)
