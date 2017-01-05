from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError


class LogForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email')


class EntryForm(FlaskForm):
    measured_on = DateField('Date')
    pounds = DecimalField('Weight')

    def validate_pounds(form, field):
        if not field.data or field.data <= 0:
            raise ValidationError('Not a valid decimal value')
