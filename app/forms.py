from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange


class NewStudentForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    classYear = IntegerField('Class Year', validators=[NumberRange(
        min = 2020, max=2030, 
        message='Please enter a valid year between 2020 and 2030')])
    track = StringField('Track', validators=[])
    mentor = StringField('Mentor\'s Name', validators=[])
    interest = StringField('Job Focus', validators=[])
    profileImage = StringField('URL to Profile Image', validators=[])
    submit = SubmitField('Add Student')
    