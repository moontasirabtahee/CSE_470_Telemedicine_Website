from models import db, Prescription, Appointment

def create_prescription(appointment_id, medicines, dosages, instructions):
    appointment = Appointment.query.get(appointment_id)
    if not appointment:
        return "Appointment not found", 404

    for medicine, dosage, instruction in zip(medicines, dosages, instructions):
        prescription = Prescription(appointment_id=appointment_id, medicine_name=medicine, dosage=dosage, instructions=instruction)
        db.session.add(prescription)

    db.session.commit()