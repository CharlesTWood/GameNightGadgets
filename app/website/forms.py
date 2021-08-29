from flask.helpers import flash
import sys
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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
    #first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    #last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    #mailing_address = StringField('Mailing Address')
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')


class PasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('newpassword')])
    submit = SubmitField('Update')