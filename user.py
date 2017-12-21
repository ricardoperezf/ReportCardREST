from flask import Flask
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hashed = db.Column(db.String(64))

    def hash(self, password):  # ENCRYPTAR LA CONTRASEÑA.
        self.password_hashed = pwd_context.encrypt(password)
