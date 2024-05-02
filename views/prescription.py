# views/patirnt.py
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required , current_user

from models import db, User, Profile, Doctor, Patient , Prescription
from controllers import user, doctor, patient,profile , prescription
from datetime import datetime

# views/prescription.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from forms import prescription
from controllers import prescription as pc

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/prescription/new/<int:appointment_id>', methods=['GET', 'POST'])
@login_required
def new_prescription(appointment_id):
    form = prescription.PrescriptionForm()
    if form.validate_on_submit():
        medicines = form.medicines.data
        dosages = form.dosages.data
        instructions = form.instructions.data
        pc.create_prescription(appointment_id=appointment_id, medicines=medicines, dosages=dosages, instructions=instructions)
    return render_template('prescription.html', form=form, appointment_id=appointment_id)