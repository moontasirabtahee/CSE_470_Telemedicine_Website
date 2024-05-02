from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class PrescriptionForm(FlaskForm):
    appointment_id = StringField('Appointment ID', validators=[DataRequired()])
    medicines = FieldList(StringField('Medicine Name', validators=[DataRequired()]), min_entries=1)
    dosages = FieldList(StringField('Dosage', validators=[DataRequired()]), min_entries=1)
    instructions = FieldList(TextAreaField('Instructions'), min_entries=1)
    submit = SubmitField('Submit')
