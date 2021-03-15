from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class ReadItemForm(FlaskForm):
    item_id = IntegerField("Item ID")
    submit = SubmitField("Look up")

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

class AddAttributeToItemForm(FlaskForm):
    item_id = IntegerField("Item ID")
    attribute_id = IntegerField("Attribute ID")
    submit = SubmitField()

class DeleteItemForm(FlaskForm):
    active_table = SelectField("Select Table To Work On", choices=["Attributes", "Item Types", "Items", "Item Attributes"])
    item_id = IntegerField("Item ID to delete")
    submit = SubmitField("Delete")

class UpdateItemTypeForm(FlaskForm):
    item_type_id = IntegerField("Item type ID")
    new_type_name = StringField("New attribute name")
    submit = SubmitField("Update")

class UpdateAttributeForm(FlaskForm):
    attribute_id = IntegerField("Attribute ID")
    new_attribute_name = StringField("New attribute name")
    new_attribute_description = StringField("New attribute description")
    submit = SubmitField("Update")

class UpdateItemForm(FlaskForm):
    item_id = IntegerField("Item ID to update")
    new_item_name = StringField("New item name")
    new_item_type = IntegerField("New item type ID")
    submit = SubmitField("Update")



