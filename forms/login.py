# Form of login with flask-wtf
# Path: forms/login.py


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms import ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired
    (), Length(min=10, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


