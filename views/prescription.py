# views/prescription.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from forms import prescription as x
from models import db, Prescription, Appointment

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/prescription/new/<int:appointment_id>', methods=['GET', 'POST'])
@login_required
def new_prescription(appointment_id):
    form = x.PrescriptionForm()
    if form.validate_on_submit():
        medicines = form.medicines.data
        dosages = form.dosages.data
        instructions = form.instructions.data

        for medicine, dosage, instruction in zip(medicines, dosages, instructions):
            prescription = Prescription(appointment_id=appointment_id, medicine_name=medicine, dosage=dosage, instructions=instruction)
            db.session.add(prescription)
        db.session.commit()

        return redirect(url_for('prescription.new_prescription', appointment_id=appointment_id))

    return render_template('prescription.html', form=form, appointment_id=appointment_id)