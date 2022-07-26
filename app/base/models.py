import jwt
from time import time
from flask import current_app
from flask_login.login_manager import LoginManager
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, event
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Roles', back_populates='role_members')
    student = db.relationship('Student', back_populates='user', uselist=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    
    def __repr__(self) -> str:
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), index=True, unique=True)
    role_members = db.relationship("User", back_populates="role")
    
    def __repr(self) -> str:
        return f'<Roles {self.name}>'

@event.listens_for(Roles.__table__, 'after_create')
def create_roles(*args, **kwargs):
    db.session.add(Roles(name='Admin'))
    db.session.add(Roles(name='Student'))
    db.session.add(Roles(name='CareerServices'))
    db.session.add(Roles(name='OtherObserver'))
    db.session.commit()
    

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('User', back_populates='student')
    
    
    firstName = db.Column(db.String(128))
    middleName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    phone = db.Column(db.String(16))
    classYear = db.Column(db.String(4))
    track = db.Column(db.String(128))
    mentor = db.Column(db.String(128))
    interest = db.Column(db.String(128))
    profileImagePath = db.Column(db.String(256))
    
    
    linkedIn = db.Column(db.String(128))
    intent = db.Column(db.String(128))
    attitude = db.Column(db.String(128))
    photo = db.Column(db.LargeBinary)
    lastUpdate = db.Column(db.DateTime)
    jobStatus = db.Column(db.String(64))
    createdDate = db.Column(db.DateTime)
    
    
    
    lampList = db.relationship('LampList', backref='student', lazy=True)
    resume = db.relationship('Resume', backref='student', lazy=True)
    education = db.relationship('Education', backref='student', lazy = True)
    infoInterviews = db.relationship('InfoInterview', backref='student', lazy = True)
    realInterviews = db.relationship('RealInterview', backref='student', lazy = True)
    mockInterviews = db.relationship('MockInterview', backref='student', lazy = True)
    jobApplications = db.relationship('JobApplication', backref='student', lazy = True)
    jobOffers = db.relationship('JobOffer', backref='student', lazy = True)
    notes = db.relationship('StudentNote', backref='student', lazy=True)
    
    
    
    def __repr__(self) -> str:
        return f'<Student: {self.firstName} {self.middleName} {self.lastName}, Class of {self.classYear}>'
    
class LampList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.DateTime)
   
    
class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    jobTitle = db.Column(db.String(128))
    compensation = db.Column(db.String(32))
    duties = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    
class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))
    school = db.Column(db.String(128))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    degree = db.Column(db.String(64))
    program = db.Column(db.String(64))
    gpa = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
    
class StudentNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    noteType = db.Column(db.String(64))
    note = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    address1 = db.Column(db.String(128))
    address2 = db.Column(db.String(128))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zipCode = db.Column(db.String(64))
    country = db.Column(db.String(64))
    numberEmployees = db.Column(db.Integer)
    relationship = db.Column(db.String(128))
    notes = db.relationship('CompanyNotes', backref='company', lazy=True)
    infoInterviews = db.relationship('InfoInterview', backref='company', lazy = True)
    realInterviews = db.relationship('RealInterview', backref='company', lazy = True)
    mockInterviews = db.relationship('MockInterview', backref='company', lazy = True)
    jobApplications = db.relationship('JobApplication', backref='company', lazy = True)
    jobOffers = db.relationship('JobOffer', backref='company', lazy = True)
    notes = db.relationship('CompanyNote', backref='student', lazy=True)
    
    def __repr__(self) -> str:
        return f'<Company: {self.name}>'
    
    
class CompanyNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    noteType = db.Column(db.String(64))
    note = db.Column(db.Text)

    
class Advocate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    email = db.Column(db.String(128))
    linkedin = db.Column(db.String(128))
    phone = db.Column(db.String(16))
    numberHelped = db.Column(db.Integer)
    companyStart = db.Column(db.DateTime)
    status = db.Column(db.String(128))


class InfoInterview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
    advocateId = db.Column(db.Integer, db.ForeignKey('advocate.id'))
    date = db.Column(db.DateTime)
    helpful = db.Column(db.String(10)) # Values should be one of: Advocate, Support, Nuteral, Detractor
    gaveRef = db.Column(db.Boolean)
    note = db.Column(db.Text)
    
class RealInterview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.DateTime)
    round = db.Column(db.String(10)) # Values should be one of: First, Second, Final, Other
    offerConfidence = db.Column(db.Integer) # Values should be 1-6
    position = db.Column(db.String(128))
    note = db.Column(db.Text)
    

class MockInterview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'))
    date = db.Column(db.DateTime)
    position = db.Column(db.String(128))
    interviewerName = db.Column(db.String(128))
    note = db.Column(db.Text)
    

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.DateTime)
    position = db.Column(db.String(128))
    interestLevel = db.Column(db.Integer) # Values should be 1-6
    confidenceLevel = db.Column(db.Integer) # Values should be 1-6
    

class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    companyId = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    date = db.Column(db.DateTime)
    position = db.Column(db.String(128))
    interestLevel = db.Column(db.Integer) # Values should be 1-6
    compensation = db.Column(db.Float)
    bonus = db.Column(db.Float)
    movingExpenses = db.Column(db.Boolean) # Maybe should be a float?
    stockOptions = db.Column(db.Boolean)
    totalPackage = db.Column(db.Float)
    intention = db.Column(db.String(32)) # Values should be one of: Will accept, Need to negotiate, Not Interested, Waiting to compare
    
