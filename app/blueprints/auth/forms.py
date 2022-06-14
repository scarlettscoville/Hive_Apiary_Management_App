from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from ...models import User
import random
from jinja2.utils import markupsafe

#FORM SECTION

class LoginForm(FlaskForm):
    email = StringField('Email Address: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = StringField('Email Address: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password', message='Passwords must match!')])
    submit = SubmitField('Register')

    icon = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/initials/{first_name}-{last_name}.svg" height="75px">')

    def validate_email(form, field):
        same_email_user = User.query.filter_by(email = field.data).first()
        if same_email_user:
            raise ValidationError('Email is already in use.')

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    email = StringField('Email Address: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password', message='Passwords must match!')])
    submit = SubmitField('Register')

    icon = markupsafe.Markup(f'<img src="https://avatars.dicebear.com/api/initials/{first_name}-{last_name}.svg" height="75px">')