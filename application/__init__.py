from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db" #"mysql+pymysql://root:19BtnEmB8NBn6Jpo@35.234.157.160/world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["WTF_CSRF_ENABLED"] = False
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "your key here"
db = SQLAlchemy(app)
from application import routes
