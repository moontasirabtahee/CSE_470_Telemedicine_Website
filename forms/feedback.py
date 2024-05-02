from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Submit')
    