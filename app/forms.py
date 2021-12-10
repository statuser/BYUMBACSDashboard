from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

class NewStudentForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phoneNumber = StringField("Phone Numbr", validators =[DataRequired()])

    classYear = IntegerField('Class Year', validators=[NumberRange(
        min = 2020, max=2030, 
        message='Please enter a valid year between 2020 and 2030')])
    track = StringField('Track', validators=[])
    mentor = StringField('Mentor\'s Name', validators=[])
    interest = StringField('Job Focus', validators=[])
    profileImage = StringField('URL to Profile Image', validators=[])
    

    #------------------------------START LinkedIn BLOCK--------------------------------------
    yn_linkedIn = RadioField("Would you like to add your LinkedIn Profile?",choices=["Yes","No"],validators=[DataRequired()])
    linkedIn = StringField('LinkedIn URL', validators=[])
    #-------------------------------END LinkedIn BLOCK---------------------------------------


    #------------------------------START Consider Self BLOCK--------------------------------------
    considerSelf = RadioField("I consider myself a...",choices=["Career Switcher","Entreprenuer","Furhter My Career", "Undecided"],validators=[DataRequired()])
    #-------------------------------END Consider Self BLOCK---------------------------------------


    #------------------------------START Recent Employer BLOCK--------------------------------------
    industry_old = StringField('Industry',validators=[DataRequired()])
    company_old = StringField('Company',validators=[DataRequired()])
    title_old = StringField('Title',validators=[DataRequired()])
    compensation = StringField('Compensation',validators=[DataRequired()])
    #-------------------------------END Recent Employer BLOCK---------------------------------------
    

    #------------------------------START Future Career BLOCK--------------------------------------
    industry_future = StringField('Industry',validators=[DataRequired()])
    company_future = StringField('Company',validators=[DataRequired()])
    title_future = StringField('Title',validators=[DataRequired()])
    #-------------------------------END Future Career BLOCK---------------------------------------
    

    #------------------------------START Past Education BLOCK--------------------------------------
    institution = StringField('School',validators=[DataRequired()])
    degree_level = SelectField("Degree Level", choices=[('hs',"High School"),("associates","Associates Degree"),("bachelors","Bachelors Degree"),("masters","Masters Degree"),("phd","PhD")])
    skills = StringField('Any "Skillz to Pay da Billz" or other Certifications?', validators=[DataRequired()])
    #-------------------------------END Past Education BLOCK---------------------------------------
    

    #------------------------------START Attitude BLOCK--------------------------------------
    attitude = RadioField("My overall attitude towards the job search is:",choices=["I have always been successful with past job searches","I have had success with my past job searches but it has taken me more time than I expected","I have struggled with my past job searches due to lack of resources/training","I have struggled with my past job searches due to external factors outside my control"],validators=[DataRequired()])
    #-------------------------------END Attitude BLOCK---------------------------------------
    

    #------------------------------START Company Interest BLOCK--------------------------------------
    lamp = StringField('Please list the top companies you are interested in recruting with:', validators=[])
    #-------------------------------END Company Interest BLOCK---------------------------------------
    

    #------------------------------START Resume Upload BLOCK--------------------------------------
    resume = FileField("Upload a current copy of your resume (.pdf or .docx)")
    #-------------------------------END Resume Upload BLOCK---------------------------------------



    submit = SubmitField('Add Student')
    