from run import db, app
from flask import url_for
from app.models.user import *

class Link(db.Model):
    id_link = db.Column(db.Integer, primary_key=True)
    name_link = db.Column(db.String(60), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    user = db.relationship('User', back_populates="links")
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    # Method to convert an object to a json
    def a_json(self):
        link_json = {
            'id_link': url_for('linkFindById', id=self.id_link, _external=True),
            'name_link': self.name_link,
            'link': self.link,
            'id_user': self.id_user
        }
        return link_json
    # Method to convert an json to a object
    @staticmethod
    def desde_json(link_json):
        name_link = link_json.get('name_link')
        link = link_json.get('link')
        id_user = link_json.get('id_user')
        return Link(
            name_link = name_link,
            link = link,
            id_user = id_user
        )