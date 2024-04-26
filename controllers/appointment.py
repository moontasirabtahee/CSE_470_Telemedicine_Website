# controllers/appointment.py
from models import db, Appointment

def create_appointment(doctor_id, patient_id, date, time, status):
    appointment = Appointment(doctor_id=doctor_id, patient_id=patient_id, date=date, time=time, status=status)
    db.session.add(appointment)
    db.session.commit()
    return appointment

def get_appointment(id):
    return Appointment.query.get(id)

def update_appointment(id, date=None, time=None, status=None):
    appointment = get_appointment(id)
    if date is not None:
        appointment.date = date
    if time is not None:
        appointment.time = time
    if status is not None:
        appointment.status = status
    db.session.commit()
    return appointment

def delete_appointment(id):
    appointment = get_appointment(id)
    db.session.delete(appointment)
    db.session.commit()

def get_all_appointments():
    return Appointment.query.all()

def get_appointment_by_doctor_id(doctor_id):
    return Appointment.query.filter_by(doctor_id=doctor_id).all()

def get_appointment_by_patient_id(patient_id):
    return Appointment.query.filter_by(patient_id=patient_id).all()

def get_appointment_by_date(date):
    return Appointment.query.filter_by(date=date).all()

def get_appointment_by_time(time):
    return Appointment.query.filter_by(time=time).all()

def get_appointment_by_status(status):
    return Appointment.query.filter_by(status=status).all()

def get_appointment_by_doctor_id_and_date(doctor_id, date):
    return Appointment.query.filter_by(doctor_id=doctor_id, date=date).all()

