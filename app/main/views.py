from flask import render_template
from . import main
from .forms import MainForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    return render_template('index.html', form=form)
