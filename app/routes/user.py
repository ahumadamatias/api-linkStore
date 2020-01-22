from run import app,db, jwt
from flask import jsonify
from flask import redirect, url_for, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from app.models.user import *
from app.controllers.user import *

@app.route('/api/users', methods=["GET"])
def getUsers():
    users = get_users()
    return jsonify({ 'Users' : [user.a_json() for user in users] })

@app.route('/api/user/<id>', methods=["GET"])
def getUserById(id):
    user = get_user_by_id(id)
    return jsonify(user.a_json())

@app.route('/api/user/signup', methods=["POST"])
def createUser():
    user = User.desde_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.a_json()), 201, {'Location': url_for('getUserById', id=user.id_user, _external=True)}

@app.route('/api/user/signin', methods=["POST"])
def singinUser():
    email = request.json.get('email_user', None)
    password = request.json.get('password_user', None)
    user = get_user_by_email(email)
    if user is not None and user.verify_password(password):
        access_token = create_access_token(identity = email)
    else:
        return jsonify({"response": "email or password incorrect!!!"})
    return jsonify(access_token = access_token), 200

@app.route('/api/user/<id>', methods=["PUT"])
def updateUser(id):
    user = get_user_by_id(id)
    user.name_user = request.json.get('name_user', user.name_user)
    user.last_name_user = request.json.get('last_name_user', user.last_name_user)
    user.email_user = request.json.get('email_user', user.email_user)
    user.password = request.json.get('password_user', user.password_user)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.a_json())

@app.route('/protected', methods=["GET"])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200