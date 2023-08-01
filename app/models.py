from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager
import jwt
import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    results = db.Column(db.Integer, default=0)

    def change_results(self, new_results):
        self.results = new_results
        db.session.add(self)
        db.session.commit()

    def generate_confirmation_token(self, expiration=3600):
        token = jwt.encode({"confirm": self.id, "exp": datetime.datetime.now(
            tz=datetime.timezone.utc) + datetime.timedelta(seconds=expiration)},
                           current_app.config["SECRET_KEY"], algorithm="HS256")
        return token

    def confirm(self, token):
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"],
                              leeway=datetime.timedelta(seconds=10),
                              algorithms=["HS256"])
        except:
            return False
        if data.get("confirm") != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    @property
    def password(self):
        raise AttributeError("Nie można odczytać atrybutu hasła")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %r>" % self.username

    def generate_reset_token(self, expiration=3600):
        token = jwt.encode({"confirm": self.id, "exp": datetime.datetime.now(
            tz=datetime.timezone.utc) + datetime.timedelta(seconds=expiration)},
                           current_app.config["SECRET_KEY"], algorithm="HS256")
        return token

    @staticmethod
    def reset_password(token, new_password):
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"],
                              leeway=datetime.timedelta(seconds=10),
                              algorithms=["HS256"])
        except:
            return False
        user = User.query.get(data.get("reset"))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
