# controllers/prescription.py
from models import db, Prescription



def create_prescription(appointment_id, medicine_name, dosage, instructions):
    prescription = Prescription(appointment_id=appointment_id, medicine_name=medicine_name, dosage=dosage, instructions=instructions)
    db.session.add(prescription)
    db.session.commit()
    return prescription

def get_prescription(id):
    return Prescription.query.get(id)

def update_prescription(id, appointment_id=None, medicine_name=None, dosage=None, instructions=None):
    prescription = get_prescription(id)
    if appointment_id is not None:
        prescription.appointment_id = appointment_id
    if medicine_name is not None:
        prescription.medicine_name = medicine_name
    if dosage is not None:
        prescription.dosage = dosage
    if instructions is not None:
        prescription.instructions = instructions
    db.session.commit()
    return prescription

def delete_prescription(id):
    prescription = get_prescription(id)
    db.session.delete(prescription)
    db.session.commit()


def get_all_prescriptions():
    return Prescription.query.all()


def get_prescription_by_appointment_id(appointment_id):
    return Prescription.query.filter_by(appointment_id=appointment_id).all()

def get_prescription_by_medicine_name(medicine_name):
    return Prescription.query.filter_by(medicine_name=medicine_name).all()

def get_prescription_by_dosage(dosage):
    return Prescription.query.filter_by(dosage=dosage).all()
