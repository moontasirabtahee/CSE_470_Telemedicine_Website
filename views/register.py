# views/register.py
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required , current_user

from models import db, User, Profile, Doctor, Patient
from controllers import user, doctor, patient,profile

from forms import registration as rg
from datetime import datetime

register = Blueprint('register', __name__)


@register.route('/register', methods=['GET', 'POST'])
def register_page():
    form = rg.RegistrationForm()

    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            return 'Username already exists'
        if User.query.filter_by(email=form.email.data).first():
            return 'Email already exists'

        Auser = user.create_user(username=form.username.data, password=form.password.data, role=form.role.data,
                    email=form.email.data, phone=form.phone.data)
        # convert date of birth to datetime object
        day = datetime.strptime(form.date_of_birth.data, '%Y-%m-%d')
        Aprofile = profile.create_profile(first_name=form.first_name.data, last_name=form.last_name.data,
                          date_of_birth=day, gender=form.gender.data, address=form.address.data,
                                          user_id=Auser.id)

        return redirect(url_for('register.register_patient'))

    return render_template('register.html', form=form)

@register.route('/register/doctor', methods=['GET', 'POST'])
@login_required
def register_doctor():
    form = rg.DoctorRegistrationForm()

    if form.validate_on_submit():
        # create doctor
        doctor.create_doctor(specialization=form.specialization.data, location=form.location.data,
                             availability=form.availability.data,profile_id=current_user.profile.id)
        return redirect(url_for('index.index_page'))

    return render_template('DocReg.html', form=form)


@register.route('/register/patient', methods=['GET', 'POST'])
@login_required
def register_patient():
    form = rg.PatientRegistrationForm()

    if form.validate_on_submit():
        # create patient
        patient.create_patient(medical_history=form.medical_history.data, profile_id=current_user.profile.id)
        return redirect(url_for('patient.patient', username=current_user.username))

    return render_template('PaiReg.html', form=form)


