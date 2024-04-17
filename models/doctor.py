# models/doctor.py

from . import db
class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    specialization = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), nullable=False)
    availability = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Doctor {}>'.format(self.id)
