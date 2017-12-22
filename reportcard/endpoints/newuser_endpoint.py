from flask import Flask, request, abort, jsonify
from reportcard import reportcard_app, db
from ..models.user import User


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
