from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField



class ReadItemTypesForm(FlaskForm):
    read_table = SelectField("Select Table To Read From", choices=["Attributes", "ItemTypes", "Items", "Item"])
    submit = SubmitField("Show Item Types")
