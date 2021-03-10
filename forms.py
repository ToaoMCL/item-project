from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



class ReadItemTypesForm(FlaskForm):
    submit = SubmitField("Show Item Types")
