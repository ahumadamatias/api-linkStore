from run import db
from flask import url_for
from app.models.link import *
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    name_user= db.Column(db.String(60), nullable=False)
    last_name_user= db.Column(db.String(60), nullable=False)
    email_user = db.Column(db.String(60), nullable=False)
    password_user = db.Column(db.String(200), nullable=False)
    links = db.relationship('Link', back_populates="user", cascade="all, delete-orphan")
    # Generation of a password hash
    @property
    def password(self):
        raise AttributeError('The password cannot be read')
    @password.setter
    def password(self, password):
        self.password_user = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_user, password)
    # Method to convert an object to a json
    def a_json(self):
        user_json = {
            'id_user': url_for('getUserById', id=self.id_user, _external=True),
            'name_user': self.name_user,
            'last_name_user': self.last_name_user,
            'email_user': self.email_user,
            'password_user': self.password_user
        }
        return user_json
    # Method to convert an json to a object
    @staticmethod
    def desde_json(user_json):
        name_user = user_json.get('name_user')
        last_name_user = user_json.get('last_name_user')
        email_user = user_json.get('email_user')
        password_user = user_json.get('password_user')
        return User(
            name_user = name_user,
            last_name_user = last_name_user,
            email_user = email_user,
            password = password_user,
        )