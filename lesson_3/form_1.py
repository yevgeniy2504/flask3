from flask_wtf import FlaskForm
from wtforms import SearchField, PasswordField, StringField
from wtforms.validators import DataRequired, Email


class LoginForms(FlaskForm):
    firstname = SearchField('Firstname', validators=[DataRequired()])
    surname = SearchField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
