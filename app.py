from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import ReadItemTypesForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:zfz800y10u9iHEzv@35.242.151.175/world"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "y45ibt4qwtfG$FCW42SAD£"

db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def home():
    form = ReadItemTypesForm()
    template = render_template("interface.html", form=form)
    return template

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
