from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, DataRequired

class HiveForm(FlaskForm):
    
    hive_name = StringField("Hive Name/ID: ")
    queen = SelectField("Queen Status: ", choices=[('Present-Active'), ('Present-NonActive'), ('Not Present')])
    health = SelectField("General Health: ", choices=[('Poor'), ('Average'), ('Good')])
    temperment = SelectField("Temperment: ", choices=[('Calm'), ('Neutral'), ('Aggressive')])
    notes = TextAreaField("Notes: ")
    submit = SubmitField("Submit")

class WeatherForm(FlaskForm):

    zip = IntegerField("Zip Code: ")
    submit = SubmitField("Search")
