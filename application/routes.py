from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application.models import Attributes, Items, ItemAttributes, ItemTypes
from application import app, db
from application.forms import ReadItemTypesForm


@app.route("/", methods=["GET", "POST"])
def home():
    form = ReadItemTypesForm()
    response = ""
    response_list = []
    if request.method == "POST":
        response = form.active_table.data     
        if form.active_table.data == "Attributes":
            response = db.session.query(Attributes).all()
            for i in response:
                response_list.append((i.id, i.name, i.description))
        if form.active_table.data == "Item Types":
            response = db.session.query(ItemTypes).all()
            for i in response:
                response_list.append((i.id, i.name))
        if form.active_table.data == "Items":
            response = db.session.query(Items).all()
            for i in response:
                response_list.append((i.id, i.name))

    template = render_template("interface.html", form=form, message=response_list)
    return template