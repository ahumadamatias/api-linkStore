from run import db
from app.models.link import *

def get_links():
    return db.session.query(Link).all()

def get_link_by_id(id):
    return db.session.query(Link).get_or_404(id)

def get_link_by_name(name):
    return db.session.query(Link).filter(Link.name_link.ilike("%" + name + "%")).first_or_404()

