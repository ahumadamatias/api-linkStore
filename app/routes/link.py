from run import app,db
from flask import jsonify
from flask import redirect, url_for, request

from app.models.link import *
from app.controllers.link import *

@app.route('/api/links', methods=["GET"])
def getLinks():
    links = get_links()
    return jsonify({ 'Links': [link.a_json() for link in links] })

@app.route('/api/link/<id>', methods=["GET"])
def getLinkById(id):
    link = get_link_by_id(id)
    return jsonify(link.a_json())

@app.route('/api/link/search/<name>', methods=["GET"])
def getLinkByName(name):
    link = get_link_by_name(name)
    return jsonify(link.a_json())


@app.route('/api/link', methods=["POST"])
def createLink():
    link = Link.desde_json(request.json)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.a_json()), 201, {'Location': url_for('getLinkById', id=link.id_link, _external=True)}

@app.route('/api/link/<id>', methods=["PUT"])
def updateLink(id):
    link = get_link_by_id(id)
    link.name_link = request.json.get('name_link', link.name_link)
    link.link = request.json.get('link', link.link)
    db.session.add(link)
    db.session.commit()
    return jsonify(link.a_json())

@app.route('/api/link/<id>', methods=["DELETE"])
def deleteLink(id):
    link = get_link_by_id(id)
    db.session.delete(link)
    db.session.commit()
    return '', 204    