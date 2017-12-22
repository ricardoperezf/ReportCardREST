from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from reportcard import reportcard_app

db = SQLAlchemy(reportcard_app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hashed = db.Column(db.String(64))

    def hash(self, password):  # ENCRYPTAR LA CONTRASEÑA.
        self.password_hashed = pwd_context.encrypt(password)


@reportcard_app.route('/register', methods=['POST'])
def register_new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    print("\n" + str(username) + " " + str(password) + "\n")
    if username is None or password is None:
        abort(400)  # MISSING USERNAME OR PASSWORD.
    if User.query.filter_by(username=username).first() is not None:
        abort(400)  # ALREADY EXISTING USER.
    user = User(username=username)
    user.hash(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

@reportcard_app.route('/si')
def test():
    return "This is just a test"