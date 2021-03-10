from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application.models import Attributes
from application import app, db
from application.forms import ReadItemTypesForm


@app.route("/", methods=["GET", "POST"])
def home():
    form = ReadItemTypesForm()
    response = ""
    if request.method == "POST":
        response = form.read_table.data
        
        if(form.read_table.data == "Attributes"):

            response = db.session.query(Attributes).all()
            response_string = ""
            for i in response:
                response_string += "<br> " + i.name
            response = response_string
    template = render_template("interface.html", form=form, message=response)
    return template