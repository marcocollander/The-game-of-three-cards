from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://marcocollander:Mqalf5942vxegs@raubuc.net/marco_collander_1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'threecards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False )
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User%r>' % self.name


@app.route('/')
def index():  
    users = User.query.all()
    print(users)
    return render_template('index.html')




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
