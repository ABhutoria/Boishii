from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField)
from wtforms.validators import InputRequired, Length

class RestaurantForm(FlaskForm):
    cName = StringField('Customer Name', validators=[InputRequired(), Length(min=2, max=100)])
    tableNum = StringField('Table No.', validators=[InputRequired(), Length(min=1)])
    restID = StringField('Restaurant ID (Ask your server)', validators=[InputRequired(), Length(min=1)])
