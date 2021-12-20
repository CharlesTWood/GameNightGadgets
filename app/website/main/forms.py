from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class Add_Cart(FlaskForm):
    quantity = DecimalField('Quantity', validators=[DataRequired()], default=1)
    submit = SubmitField('Add To Cart')