# models/patient.py
from . import db
class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Patient {}>'.format(self.id)
