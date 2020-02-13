from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class InputTextForm(FlaskForm):
    text = TextAreaField('Your text', validators=[DataRequired()])
    submit = SubmitField('Send')