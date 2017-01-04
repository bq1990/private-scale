from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired


class TrackerForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email')


class MeasurementForm(FlaskForm):
    measured_on = DateField('Date', validators=[DataRequired()])
    pounds = DecimalField('Weight', validators=[DataRequired()])
