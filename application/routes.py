from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application.models import Attributes, Items, ItemAttributes, ItemTypes
from application import app, db
from application.forms import InstructionDefenitionForm, CreateAttributeForm, CreateItemTypeForm, CreateItemForm, DeleteItemForm

def GetDbTableNameFromPassedValue(value):
    if value == "Attributes":
        return Attributes
    elif value == "Item Types":
        return ItemTypes
    elif value == "Items":
        return Items
    else:
        return None

'''
Template HTML files to re-route based on what task they are performing 
'''

@app.route("/", methods=["GET", "POST"])
@app.route("/read", methods=["GET", "POST"])
def read():
    instruction_form = InstructionDefenitionForm()
    response = instruction_form.active_table.data
    response_list = []
    if instruction_form.active_table.data == "Attributes":
        response = db.session.query(Attributes).all()
        for i in response:
            response_list.append((i.id, i.name, i.description))
    elif instruction_form.active_table.data == "Item Types":
        response = db.session.query(ItemTypes).all()
        for i in response:
            response_list.append((i.id, i.name))
    elif instruction_form.active_table.data == "Items":
        response = db.session.query(Items).all()
        for i in response:
            response_list.append((i.id, i.name))

    template = render_template("read.html", form=instruction_form, message=response_list)
    return template

@app.route("/create", methods=["GET", "POST"])
def create():
    instruction_form = InstructionDefenitionForm()
    create_item_type_form = None
    if instruction_form.active_table.data == "Attributes":
        create_item_type_form = CreateAttributeForm()
    elif instruction_form.active_table.data == "Item Types":
        create_item_type_form = CreateItemTypeForm()
    elif instruction_form.active_table.data == "Items":
        create_item_type_form = CreateItemForm()
    template = render_template("create.html", form=instruction_form, create_form=create_item_type_form)
    return template

@app.route("/update", methods=["GET", "POST"])
def update():
    return "update"

@app.route("/delete", methods=["GET", "POST"])
def delete():
    instruction_form = InstructionDefenitionForm()
    delete_form = DeleteItemForm()
    if request.method == "POST":
        table = GetDbTableNameFromPassedValue(instruction_form.active_table.data)
        item = table.query.filter_by(id=delete_form.item_id.data).first()
        db.session.delete(item)
        db.session.commit()

    template = render_template("delete.html", form=instruction_form, delete_form=delete_form)
    return template