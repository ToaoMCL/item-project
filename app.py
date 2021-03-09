from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:zfz800y10u9iHEzv@35.242.151.175/world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "home"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
