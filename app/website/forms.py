from flask.helpers import flash
import sys
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import TelField

from website.enums import USStateEnum


def Password_complexity(form, field):
    special_chars = '!@#$%^&*()_-+=[]|\/?>.<,|'
    valid = False
    for char in field.data:
        if valid == False:
            for special in special_chars:
                if char == special: valid = True  
    if valid == False:
        raise ValidationError('Password must contain at lease one special character')


class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    #remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Registerform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    #first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    #last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    #mailing_address = StringField('Mailing Address')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')


class Accountform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')


class PasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update')

class AddressForm(FlaskForm):
    choices = USStateEnum
    name = StringField('Name on address', validators=[DataRequired(), Length(max=20)])
    phone_number = TelField('Contact Phone #', validators=[Length(max=14)])
    address = StringField('Your address', validators=[DataRequired(), Length(max=30)])
    city = StringField('City', validators=[DataRequired(), Length(max=20)])
    organization = StringField('Organization Name', validators=[Length(max=20)])
    po_box = StringField('P.O Box', validators=[DataRequired(), Length(max=20)])
    state = SelectField('State', choices=[(choice.name, choice.value) for choice in choices])
    zip_code = StringField('Postal Code', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Add address')


