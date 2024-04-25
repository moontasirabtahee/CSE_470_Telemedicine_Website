from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError
from models import User, Doctor, Patient, Profile

class RegistrationForm(FlaskForm):
    # user details
    username = StringField('Username', validators=[DataRequired(), Length(min=10, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('doctor', 'Doctor'), ('patient', 'Patient')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = StringField('Date of Birth', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male',"Male"),('female',"Female")])
    address = StringField('Address', validators=[DataRequired()])

    submit = SubmitField('Sign Up')
class DoctorRegistrationForm(RegistrationForm):
    # doctor-specific fields
    specialization = StringField('Specialization', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    availability = StringField('Availability', validators=[DataRequired()])

class PatientRegistrationForm(RegistrationForm):
    # patient-specific fields
    medical_history = StringField('Medical History', validators=[DataRequired()])

    # def validate_username(self, field):


