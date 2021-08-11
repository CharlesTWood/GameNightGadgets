import flask
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

def Password_complexity(form, field):
    special_chars = '!@#$%^&*()_-+=[]|\/?>.<,|'
    check_chars = field.data.find(special_chars)
    if check_chars == -1:
        raise ValidationError('Password must contain at least one special character')

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Registerform(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    mailing_address = StringField('Mailing Address')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Password_complexity, Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')