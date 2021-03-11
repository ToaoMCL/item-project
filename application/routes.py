from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application.models import Attributes, Items, ItemAttributes, ItemTypes
from application import app, db
from application.forms import InstructionDefenitionForm, CreateAttributeForm, CreateItemTypeForm, CreateItemForm


@app.route("/", methods=["GET", "POST"])
def home():
    instruction_form = InstructionDefenitionForm()
    create_item_type_form = None
    response = ""
    response_list = []
    if request.method == "POST":
        response = instruction_form.active_table.data     
        if instruction_form.active_table.data == "Attributes":
            create_item_type_form = CreateAttributeForm()
            response = db.session.query(Attributes).all()
            for i in response:
                response_list.append((i.id, i.name, i.description))
        if instruction_form.active_table.data == "Item Types":
            create_item_type_form = CreateItemTypeForm()
            response = db.session.query(ItemTypes).all()
            for i in response:
                response_list.append((i.id, i.name))
        if instruction_form.active_table.data == "Items":
            create_item_type_form = CreateItemForm()
            response = db.session.query(Items).all()
            for i in response:
                response_list.append((i.id, i.name))

    template = render_template("interface.html", form=instruction_form, create_form=create_item_type_form, message=response_list)
    return template