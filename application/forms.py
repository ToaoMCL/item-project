from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField



class ReadItemTypesForm(FlaskForm):
    active_table = SelectField("Select Table To Read From", choices=["Attributes", "Item Types", "Items"])
    submit = SubmitField("Show Table Contents")
