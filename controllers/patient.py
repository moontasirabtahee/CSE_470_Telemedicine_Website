# controllers/patient.py
from models import db, Patient

def create_patient(profile_id, medical_history):
    patient = Patient(profile_id=profile_id, medical_history=medical_history)
    db.session.add(patient)
    db.session.commit()
    return patient

def get_patient(id):
    return Patient.query.get(id)

def update_patient(id, profile_id=None, medical_history=None):
    patient = get_patient(id)
    if profile_id is not None:
        patient.profile_id = profile_id
    if medical_history is not None:
        patient.medical_history = medical_history
    db.session.commit()
    return patient

def delete_patient(id):
    patient = get_patient(id)
    db.session.delete(patient)
    db.session.commit()


def get_all_patients():
    return Patient.query.all()

def get_patient_by_profile_id(profile_id):
    return Patient.query.filter_by(profile_id=profile_id).first()


def get_appointment_by_patient_id(id):
    from models import Appointment
    return Appointment.query.filter_by(patient_id=id).all()
