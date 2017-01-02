from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class TrackerForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
