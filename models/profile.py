
# models/profile.py
from . import db
class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    doctor = db.relationship('Doctor', backref='profile', uselist=False)
    patient = db.relationship('Patient', backref='profile', uselist=False)


    def __repr__(self):
        return '<Profile {}>'.format(self.id)
