from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:zfz800y10u9iHEzv@35.242.151.175/world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "y45ibt4qwtfG$FCW42SAD£"

db = SQLAlchemy(app)
from application import routes
