from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField



class InstructionDefenitionForm(FlaskForm):
    active_table = SelectField("Select Table To Work On", choices=["Attributes", "Item Types", "Items"])
    mode_select = SelectField("Interaction Mode", choices=["Create", "Read", "Update", "Delete"])
    submit = SubmitField("Update Settings")

class CreateAttributeForm(FlaskForm):
    attribute_name = StringField("Attribute Name")
    attribute_description = StringField("Attribute Description")
    submit = SubmitField("Create New Attribute")

class CreateItemTypeForm(FlaskForm):
    item_type_name = StringField("Item Type Name")
    submit = SubmitField("Create New Item Type")

class CreateItemForm(FlaskForm):
    item_name = StringField("Item Name")
    item_type = IntegerField("Item Type ID")
    submit = SubmitField("Create New Item")

class DeleteItemForm(FlaskForm):
    item_id = IntegerField("Item id to delete from")
    submit = SubmitField("Delete")


