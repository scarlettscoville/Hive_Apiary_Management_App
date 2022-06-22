from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class HiveForm(FlaskForm):
    
    name = StringField("Hive Name/ID: ")
    queen = SelectField("Queen Status: ", choices=[('Present-Active'), ('Present-NonActive'), ('Not Present')], validators=DataRequired())
    health = SelectField("General Health: ", choices=[('Poor'), ('Average'), ('Good')], validators=DataRequired())
    temperment = SelectField("Temperment: ", choices=[('Calm'), ('Neutral'), ('Aggressive')], validators=DataRequired())
    notes = TextAreaField("Notes: ")
    submit = SubmitField("Submit")
