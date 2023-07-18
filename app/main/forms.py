from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    number_of_hits = StringField("Ilość trafień: ", validators=[DataRequired()])
    number_of_attempts = StringField("Ilość prób: ", validators=[DataRequired()])
    hit_percentage = StringField("Procent trafień: ", validators=[DataRequired()])
    submit = SubmitField("Wyślij")
