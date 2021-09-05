
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import TelField

from website.account_menu.enums import USStateEnum
from website.user.utilities import Password_complexity

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
    name = StringField('Name on address', validators=[DataRequired(), Length(max=20)])
    phone_number = TelField('Contact Phone #', validators=[Length(max=14)])
    address = StringField('Your address', validators=[DataRequired(), Length(max=30)])
    city = StringField('City', validators=[DataRequired(), Length(max=20)])
    organization = StringField('Organization Name', validators=[Length(max=20)])
    po_box = StringField('P.O Box', validators=[Length(max=20)])
    state = SelectField('State', choices=[(choice.name, choice.value) for choice in USStateEnum])
    zip = StringField('Postal Code', validators=[DataRequired(), Length(max=20)])
    submit = SubmitField('Add address')