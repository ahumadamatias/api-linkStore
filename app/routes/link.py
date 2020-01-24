from run import app,db
from flask import jsonify
from flask import redirect, url_for, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from app.models.link import *
from app.controllers.link import *

@app.route('/api/links', methods=["GET"])
@jwt_required
def getLinks():
    links = get_links()
    return jsonify({ 'Links': [link.a_json() for link in links] })

@app.route('/api/link/<id>', methods=["GET"])
@jwt_required
def getLinkById(id):
    link = get_link_by_id(id)
    return jsonify(link.a_json())

@app.route('/api/link/search/<name>', methods=["GET"])
@jwt_required
def getLinkByName(name):
    links = get_link_by_name(name)
    return jsonify({ 'Links' : [ link.a_json() for link in links ]})


@app.route('/api/link', methods=["POST"])
@jwt_required
def createLink():
    link = Link.desde_json(request.json)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.a_json()), 201, {'Location': url_for('getLinkById', id=link.id_link, _external=True)}

@app.route('/api/link/<id>', methods=["PUT"])
@jwt_required
def updateLink(id):
    link = get_link_by_id(id)
    link.name_link = request.json.get('name_link', link.name_link)
    link.link = request.json.get('link', link.link)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.a_json())

@app.route('/api/link/<id>', methods=["DELETE"])
@jwt_required
def deleteLink(id):
    link = get_link_by_id(id)
    db.session.delete(link)
    db.session.commit()
    return '', 204    