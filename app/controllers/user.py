from run import db
from app.models.user import *

def get_users():
    return db.session.query(User).all()

def get_user_by_id(id):
    return db.session.query(User).get(id)

def get_user_by_email(email):
    return db.session.query(User).filter(User.email_user == email).first()