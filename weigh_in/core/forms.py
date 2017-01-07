from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError


class LogForm(FlaskForm):
    name = StringField('Weight Log Title', validators=[DataRequired()])
    recaptcha = RecaptchaField()


class EntryForm(FlaskForm):
    measured_on = StringField('Date')
    pounds = DecimalField('Weight')

    def validate_pounds(form, field):
        if not field.data or field.data <= 0:
            raise ValidationError('Not a valid decimal value')
