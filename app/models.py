from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(32), index=True, nullable=False)
    lastName = db.Column(db.String(32), index=True, nullable=False)
    classYear = db.Column(db.Integer)
    track = db.Column(db.String(32), index=True)
    mentor = db.Column(db.String(64), index=True)
    interest = db.Column(db.String(32))
    profileImage = db.Column(db.String(128))
    
    def __repr__(self) -> str:
        return f'Student <{self.firstName} {self.lastName}>'
    