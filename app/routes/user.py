from run import app,db, jwt
from flask import jsonify
from flask import redirect, url_for, request

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

@app.route('/api/user/singup', methods=["POST"])
def createUser():
    user = User.desde_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.a_json()), 201, {'Location': url_for('getUserById', id=user.id_user, _external=True)}

@app.route('/api/user/<id>', methods=["PUT"])
def updateUser(id):
    user = get_user_by_id(id)
    user.name_user = request.json.get('name_user', user.name_user)
    user.last_name_user = request.json.get('last_name_user', user.last_name_user)
    user.email_user = request.json.get('name_user', user.name_user)
    user.password = request.json.get('name_user', user.name_user)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.a_json())