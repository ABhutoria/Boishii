from flask_wtf import FlaskForm
from wtforms import StringField

class RegistrationForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired(),Length(min= 2, max = 30)])
    table = StringField('Table', 