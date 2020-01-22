import os
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') #clave secreta
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+os.getenv('DB_USERNAME')+':'+os.getenv('DB_PASS')+'@localhost/linkStore-db'

db = SQLAlchemy(app)
mail = Mail(app)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})