from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired

class InspectionForm(FlaskForm):
    
    date = DateField("Date of Inspection: ", validators=[DataRequired()])
    colony_condition = SelectField("Colony Condition: ", choices=[('Poor'), ('Average'), ('Good')], validators=DataRequired())
    activity = SelectField("Activity: ", choices=[('Low'), ('Average'), ('High')], validators=DataRequired())
    laying_pattern = SelectField("Laying Pattern: ", choices=[('Poor'), ('Patchy'), ('Solid')], validators=DataRequired())
    temperment = SelectField("Temperment: ", choices=[('Calm'), ('Neutral'), ('Aggressive')], validators=DataRequired())
    visible = SelectMultipleField("Visible (select all that apply): ", choices=[('Eggs'), ('Larvae'), ('Capped Cells'), ('Queen Cells')])
    notes = TextAreaField("Notes: ")
    submit = SubmitField("Submit")
