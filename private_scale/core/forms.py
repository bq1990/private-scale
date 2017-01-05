from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired


class LogForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email')


class EntryForm(FlaskForm):
    measured_on = DateField('Date', validators=[DataRequired()])
    pounds = DecimalField('Weight', validators=[DataRequired()])
