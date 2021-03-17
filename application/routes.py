from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from application.models import Attributes, Items, ItemAttributes, ItemTypes
from application import app, db
from application.forms import ReadItemForm, AddAttributeToItemForm, CreateAttributeForm, CreateItemTypeForm, CreateItemForm, DeleteItemForm, UpdateAttributeForm, UpdateItemForm, UpdateItemTypeForm
from application.extra_functions import GetDbTableNameFromPassedValue

@app.route("/")
@app.route("/read")
def read():
    return render_template("read.html", message="")

@app.route("/read/item types")
def read_item_types():
    response_list = []
    response = db.session.query(ItemTypes).all()
    for i in response:
        response_list.append((i.id, i.name))   
    return render_template("read.html", message=response_list)


@app.route("/read/attributes")
def read_attributes():
    response_list = []
    response = db.session.query(Attributes).all()
    for i in response:
        response_list.append((i.id, i.name, i.description))
    return render_template("read.html", message=response_list)

@app.route("/read/items")
def read_items():
    response_list = []
    response = db.session.query(Items).all()
    for i in response:
        response_list.append((i.id, i.name, ItemTypes.query.filter_by(id=i.fk_item_type).first().name)) 
    return render_template("read.html", message=response_list)

@app.route("/read/item", methods=["GET", "POST"])
def read_item():
    response_list = []
    read_item_form = ReadItemForm()
    if read_item_form.validate_on_submit():
        item = Items.query.filter_by(id=read_item_form.item_id.data).first()
        item_type = ItemTypes.query.filter_by(id=item.fk_item_type).first()
        response_list.append((item.name, item_type.name)) 
        item_attributes = ItemAttributes.query.filter_by(fk_item_id=item.id).all()
        for attribute in item_attributes:
            attribute_values = Attributes.query.filter_by(id=attribute.fk_attribute_id).first()
            response_list.append((attribute_values.name, attribute_values.description))
    return render_template("read item.html",read_item=read_item_form, message=response_list)


@app.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")

@app.route("/create/attribute", methods=["GET", "POST"])
def create_attribute():
    create_form = CreateAttributeForm()
    if create_form.validate_on_submit():
        db.session.add(Attributes(name=create_form.attribute_name.data, description=create_form.attribute_description.data))
        db.session.commit()
    return render_template("create attribute.html", create_form=create_form)

@app.route("/create/type", methods=["GET", "POST"])
def create_type():
    create_form = CreateItemTypeForm()
    if create_form.validate_on_submit():
        db.session.add(ItemTypes(name=create_form.item_type_name.data))
        db.session.commit()
    return render_template("create type.html", create_form=create_form)

@app.route("/create/item", methods=["GET", "POST"])
def create_item():
    create_form = CreateItemForm()
    if create_form.validate_on_submit():
        db.session.add(Items(name=create_form.item_name.data, fk_item_type=create_form.item_type.data))   
        db.session.commit()
    return render_template("create item.html", create_form=create_form)

@app.route("/create/add attribute", methods=["GET", "POST"])
def create_attribute_link():
    create_form = AddAttributeToItemForm()
    if create_form.validate_on_submit():
        db.session.add(ItemAttributes(fk_item_id=create_form.item_id.data ,fk_attribute_id=create_form.attribute_id.data))
        db.session.commit()
    return  render_template("create item attribute link.html", create_form=create_form)


@app.route("/update", methods=["GET", "POST"])
def update():
    return render_template("update.html")

@app.route("/update/attribute", methods=["GET", "POST"])
def update_attribute():
    update_form = UpdateAttributeForm()
    if update_form.validate_on_submit():
        attribute = Attributes.query.filter_by(id=update_form.attribute_id.data).first()
        if update_form.new_attribute_name.data != "":
            attribute.name = update_form.new_attribute_name.data
        if update_form.new_attribute_description.data != "":
            attribute.description = update_form.new_attribute_description.data
        db.session.commit()
    return render_template("update attribute.html", update_form=update_form)

@app.route("/update/type", methods=["GET", "POST"])
def update_type():
    update_form = UpdateItemTypeForm()
    if update_form.validate_on_submit():
        item_type = ItemTypes.query.filter_by(id=update_form.item_type_id.data).first()
        item_type.name = update_form.new_type_name.data
        db.session.commit()
    return render_template("update type.html", update_form=update_form)

@app.route("/update/item", methods=["GET", "POST"])
def update_item():
    update_form = UpdateItemForm()
    if update_form.validate_on_submit():
        item = Items.query.filter_by(id=update_form.item_id.data).first()
        if update_form.new_item_name.data != "":
            item.name = update_form.new_item_name.data
      # I couldn't find a way to change the fk on this object
      # if update_form.new_item_type.data != None:
      #     item.fk_item_type_id = ItemTypes.query.filter_by(id=update_form.new_item_type.data).first() 
        db.session.commit()
    return render_template("update item.html", update_form=update_form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    delete_form = DeleteItemForm()
    if delete_form.validate_on_submit():
        table = GetDbTableNameFromPassedValue(delete_form.active_table.data)
        item = table.query.filter_by(id=delete_form.item_id.data).first()
        db.session.delete(item)
        db.session.commit()

    template = render_template("delete.html", delete_form=delete_form)
    return template