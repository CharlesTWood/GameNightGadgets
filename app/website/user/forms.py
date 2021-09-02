from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from website.user.utilities import Password_complexity

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    #remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Registerform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    #first_name = StringField('First Name', validators=[DataRequired(), Length(max=20)])
    #last_name = StringField('Last Name', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20), Password_complexity])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')