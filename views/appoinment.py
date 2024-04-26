from flask import Flask , request, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

from models import db, User, Profile, Doctor, Patient
from controllers import doctor as d
from controllers import profile , user

from forms import registration as rg , login as lg , doctorF as dg
appointment = Blueprint('appointment', __name__)
from datetime import datetime
@appointment.route('/appointments/create/<int:doctor_id>', methods=['GET', 'POST'])
@login_required
def create_appointment(doctor_id):
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        date = datetime.strptime(date, '%Y-%m-%d').date()
        time = datetime.strptime(time, '%H:%M').time()
        from controllers import appointment as ap
        ap.create_appointment(doctor_id=doctor_id, patient_id=current_user.id, date=date, time=time, status="Scheduled")
        return redirect(url_for('patient.patient', username=current_user.username))
    else:
        return render_template('create_appoinment.html',doctor_id=doctor_id)


#view all appointments for the current user
@appointment.route('/appointments', methods=['GET'])
@login_required
def appointments():
    from controllers import appointment as ap
    appointments = ap.get_appointment_by_patient_id(current_user.id)
    return render_template('appointments.html', appointments=appointments)

@appointment.route('/appointments/delete/<int:id>', methods=['GET'])
@login_required
def delete(id):
    from controllers import appointment as ap
    ap.delete_appointment(id)
    return redirect(url_for('appointment.appointments'))

@appointment.route('/appointments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    from controllers import appointment as ap
    appointment = ap.get_appointment(id)
    if request.method == 'POST':
        date = request.form.get('date')
        time = request.form.get('time')
        date = datetime.strptime(date, '%Y-%m-%d').date()
        time = datetime.strptime(time, '%H:%M').time()
        ap.update_appointment(id=id, date=date, time=time)
        return redirect(url_for('appointment.appointments'))
    else:
        return render_template('edit_appointment.html', appointment=appointment)
