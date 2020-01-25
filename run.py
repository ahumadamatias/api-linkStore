import os
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') #clave secreta
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+os.getenv('DB_USERNAME')+':'+os.getenv('DB_PASS')+'@localhost/linkStore-db'
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
jwt = JWTManager (app)
mail = Mail(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    from app.routes.link import *
    from app.routes.user import *
    app.run(port = 5000, debug = True)
