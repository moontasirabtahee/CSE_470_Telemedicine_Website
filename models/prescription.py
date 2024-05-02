# models/prescription.py
from . import db

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    medicine_name = db.Column(db.String(64), nullable=False)
    dosage = db.Column(db.String(64), nullable=False)
    instructions = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Prescription {}>'.format(self.id)