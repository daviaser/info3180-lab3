from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), DataRequired()])
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired(), DataRequired()])
    message = TextAreaField('Message', validators=[InputRequired(), DataRequired()])