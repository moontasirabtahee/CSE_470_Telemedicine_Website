# controllers/doctor.py
from models import db, Doctor

def create_doctor(profile_id, specialization, location, availability):
    doctor = Doctor(profile_id=profile_id, specialization=specialization, location=location, availability=availability)
    db.session.add(doctor)
    db.session.commit()
    return doctor

def get_doctor(id):
    return Doctor.query.get(id)

def update_doctor(id, profile_id=None, specialization=None, location=None, availability=None):
    doctor = get_doctor(id)
    if profile_id is not None:
        doctor.profile_id = profile_id
    if specialization is not None:
        doctor.specialization = specialization
    if location is not None:
        doctor.location = location
    if availability is not None:
        doctor.availability = availability
    db.session.commit()
    return doctor

def delete_doctor(id):
    doctor = get_doctor(id)
    db.session.delete(doctor)
    db.session.commit()

def get_all_doctors():
    return Doctor.query.all()

def get_doctor_by_specialization(specialization):
    return Doctor.query.filter_by(specialization=specialization).all()

def get_doctor_by_location(location):
    return Doctor.query.filter_by(location=location).all()

def get_doctor_by_availability(availability):
    return Doctor.query.filter_by(availability=availability).all()

def get_doctor_by_profile_id(profile_id):
    return Doctor.query.filter_by(profile_id=profile_id).first()
