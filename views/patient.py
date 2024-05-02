# views/patirnt.py
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required , current_user

from models import db, User, Profile, Doctor, Patient
from controllers import user, doctor, patient,profile
from datetime import datetime


patient_bp = Blueprint('patient', __name__)

#route should be /patients/username
@patient_bp.route('/patients/<username>', methods=['GET'])
@login_required
def patient(username):
    #get all the doctors from the database with joining with the profile table
    doctors = Doctor.query.join(Profile).all()
    user = User.query.filter_by(username=username).first()
    from controllers import patient
    
    appointments = patient.get_appointment_by_patient_id(current_user.id)
    # appointments to the doctor
    if appointments:
        doctorx = Doctor.query.filter_by(id=appointments[0].doctor_id)
        # profile of the doctor
        profilex = Profile.query.filter_by(id=doctorx[0].profile_id).first()
    return render_template('patient.html', doctors=doctors, user=user, appointments=appointments, App_doctor=doctorx, App_profile=profilex)

from forms import patientF
from datetime import datetime
@patient_bp.route('/patient/edit/<username>', methods=['GET', 'POST'])
@login_required
def update_patient(username=None):
    # Get the user, profile, and patient details using the current user's ID
    userx = User.query.filter_by(id=current_user.id).first()
    profilex = Profile.query.filter_by(user_id=current_user.id).first()
    patientx = Patient.query.filter_by(profile_id=profilex.id).first()

    if userx is None or profilex is None or patientx is None:
        # Handle the case where no user, profile, or patient is found
        return "No user, profile, or patient found", 404

    if request.method == 'POST':
        # Update user
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        from controllers import user
        user.update_user(id=userx.id, username=username, email=email, phone=phone)

        # Update profile
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = datetime.strptime(request.form.get('date_of_birth'), '%Y-%m-%d')
        gender = request.form.get('gender')
        address = request.form.get('address')
        from controllers import profile
        profile.update_profile(id=profilex.id,user=userx.id , first_name=first_name, last_name=last_name,
                               date_of_birth=date_of_birth,gender=gender, address=address)

        # Update patient
        medical_history = request.form.get('medical_history')
        from controllers import patient
        patient.update_patient(id=patientx.id, medical_history=medical_history)

        return redirect(url_for('patient.patient', username=userx.username))

    form = patientF.EditPatientForm(obj=userx)  # Populate the form with the current details
    return render_template('edit_patient.html', form=form, patient=patientx,user = userx, profile = profilex)

