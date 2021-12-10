from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class NewStudentForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
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







class WeeklyReportForm(FlaskForm):
    feeling = RadioField("Before we jump in... How are you FEELING about recruting? 1 - HELP! 6 - I've got this! ",choices=[1,2,3,4,5,6],validators=[DataRequired()])

    #-----------------------------------------------------------------------
    #--------------------- START APPLY BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_apply = RadioField("Did you APPLY for any jobs this week?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    int_apply = IntegerField('How many jobs did you APPLY for this week?', validators=[NumberRange(
        min = 1, 
        message ='Please enter a valid number greater than 0')])
    apply_company = StringField('Which companies did you APPLY for this week?', validators=[])
    #---------------------- END APPLY BLOCK -----------------------



    #-----------------------------------------------------------------------
    #--------------------- START INFO INTERVIEW BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_info = RadioField("Did you have any INFO interviews this week?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    int_info = IntegerField('How many INFO interviews did you have this week?', validators=[NumberRange(
        min = 1, 
        message ='Please enter a valid number greater than 0')])
    info_company = StringField('What companies did you INFO interview with this week?', validators=[])
    #---------------------- END INFO INTERVIEW BLOCK -----------------------



    #-----------------------------------------------------------------------
    #--------------------- START REAL INTERVIEW BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_real = RadioField("Did you have any REAL interviews this week?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    int_real = IntegerField('How many REAL interviews did you have this week?', validators=[NumberRange(
        min = 1, 
        message ='Please enter a valid number greater than 0')])
    real_company = StringField('What companies did you INTERVIEW with this week?', validators=[])
    #---------------------- END REAL INTERVIEW BLOCK -----------------------



    #-----------------------------------------------------------------------
    #--------------------- START INFO SESSION BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_info_session = RadioField("Did you attend any INFO SESSIONS this week?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    int_info_session = IntegerField('How many INFO SESSIONS did you have this week?', validators=[NumberRange(
        min = 1, 
        message ='Please enter a valid number greater than 0')])
    info_session_company = StringField('What companies did you attended INFO SESSIONS for this week?', validators=[])
    #---------------------- END INFO SESSION BLOCK -----------------------



    #-----------------------------------------------------------------------
    #--------------------- START OFFERS BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_offers = RadioField("Did you recive any internship or job OFFERS this week?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    offer_company = StringField('What companies did you recieve OFFERS from this week?', validators=[])
    #---------------------- END OFFERS BLOCK -----------------------
    


    #-----------------------------------------------------------------------
    #--------------------- START FEEDBACK BLOCK ----------------------
    #-----------------------------------------------------------------------
    yn_feedback = RadioField("Do you have any thoughts for Career Services?",choices=["Yes","No"],validators=[DataRequired()])
    # -------------------------- IF YES --------------------------- 
    feedback = StringField('What can we do for you this week?', validators=[])
    #---------------------- END FEEDBACK BLOCK -----------------------
    submit = SubmitField('Submit KPIs')
    
   