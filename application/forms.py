from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application.custom_validation import IsNumericCheck, ExistsInDbCheck, SymbolCheck

class ReadItemForm(FlaskForm):
    item_id = IntegerField(
        "Item ID", 
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck(table="Items")
    ])
    submit = SubmitField("Look up")


class CreateAttributeForm(FlaskForm):
    attribute_name = StringField(
        "Attribute Name",
         validators=[DataRequired(),
                    SymbolCheck()
    ])

    attribute_description = StringField(
        "Attribute Description",
        validators=[DataRequired(),
                    SymbolCheck()
    ])
    submit = SubmitField("Create New Attribute")


class CreateItemTypeForm(FlaskForm):
    item_type_name = StringField(
        "Item Type Name", 
        validators=[DataRequired(),
                    SymbolCheck()
    ])
    submit = SubmitField("Create New Item Type")


class CreateItemForm(FlaskForm):
    item_name = StringField(
    "Item Name", 
    validators=[DataRequired(),
                    SymbolCheck()
    ])
    item_type = IntegerField("Item Type ID", 
    validators=[DataRequired(),
                IsNumericCheck()
    ])
    submit = SubmitField("Create New Item")


class AddAttributeToItemForm(FlaskForm):
    item_id = IntegerField(
        "Item ID", 
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck(table="Items")])

    attribute_id = IntegerField(
        "Attribute ID",
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck(table="Attributes")])
    submit = SubmitField()


class DeleteItemForm(FlaskForm):
    active_table = SelectField(
        "Select Table To Work On", 
        choices=["Attributes",
                "Item Types",
                "Items", 
                "Item Attributes"])

    item_id = IntegerField(
        "Item ID to delete",
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck()])
    submit = SubmitField("Delete")


class UpdateItemTypeForm(FlaskForm):
    item_type_id = IntegerField("Item type ID",
                                validators=[DataRequired(),
                                            IsNumericCheck(),
                                            ExistsInDbCheck(table="Item Types")])

    new_type_name = StringField("New attribute name",
                                validators=[DataRequired(),
                                            SymbolCheck()])
    submit = SubmitField("Update")


class UpdateAttributeForm(FlaskForm):
    attribute_id = IntegerField(
        "Attribute ID", 
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck(table="Attributes")])

    new_attribute_name = StringField(
        "New attribute name", 
        validators=[DataRequired(),
                    SymbolCheck()])

    new_attribute_description = StringField(
        "New attribute description", 
        validators=[DataRequired(),
                    SymbolCheck()])
    submit = SubmitField("Update")


class UpdateItemForm(FlaskForm):
    item_id = IntegerField(
        "Item ID to update", 
        validators=[DataRequired(),
                    IsNumericCheck(),
                    ExistsInDbCheck(table="Items")])

    new_item_name = StringField(
        "New item name", 
        validators=[DataRequired()])
    # new_item_type = IntegerField("New item type ID", validators=[
    #     DataRequired(),
    #     IsNumericCheck()
    # 
    submit = SubmitField("Update")
