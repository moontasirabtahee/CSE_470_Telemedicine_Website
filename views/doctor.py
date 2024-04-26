from flask import Flask , request, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

from models import db, User, Profile, Doctor, Patient
from controllers import doctor as d
from controllers import profile , user

from forms import registration as rg , login as lg , doctorF as dg

doctor = Blueprint('doctor', __name__)

@doctor.route('/doctor/<username>', methods=['GET', 'POST'])
@login_required
def doctor_page(username=None):
    # Get the user, profile, and doctor details using the current user's ID
    userx = User.query.filter_by(id=current_user.id).first()
    profilex = Profile.query.filter_by(user_id=current_user.id).first()
    doctorx = Doctor.query.filter_by(profile_id=profilex.id).first()

    if user is None or profile is None or doctor is None:
        # Handle the case where no user, profile, or doctor is found
        return "No user, profile, or doctor found", 404

    return render_template('doctor.html', user=userx, profile=profilex, doctor=doctorx)



from forms import doctorF
from datetime import datetime
@doctor.route('/doctor/edit/<username>', methods=['GET', 'POST'])
@login_required
def update_doctor(username=None):
    # Get the user, profile, and doctor details using the current user's ID
    userx = User.query.filter_by(id=current_user.id).first()
    profilex = Profile.query.filter_by(user_id=current_user.id).first()
    doctorx = Doctor.query.filter_by(profile_id=profilex.id).first()

    if userx is None or profilex is None or doctorx is None:
        # Handle the case where no user, profile, or doctor is found
        return "No user, profile, or doctor found", 404

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



        # Update doctor
        specialization = request.form.get('specialization')
        location = request.form.get('location')
        availability = request.form.get('availability')
        from controllers import doctor
        doctor.update_doctor(id=doctorx.id, specialization=specialization, location=location,
                             availability=availability)

        # Commit the changes to the database


        return redirect(url_for('doctor.doctor_page', username=userx.username))

    form = doctorF.EditDoctorForm(obj=userx)  # Populate the form with the current details
    return render_template('edit_doctor.html', form=form, doctor=doctorx,user = userx, profile = profilex)

@doctor.route('/doctor/delete/<username>', methods=['GET', 'POST'])
def delete_doctor(id):
    # delete the profile and user as well
    doc = d.get_doctor_by_profile_id(id)
    profile_id = doc.profile_id
    user_id = profile.get_profile(profile_id).user_id
    d.delete_doctor(id)
    profile.delete_profile(profile_id)
    user.delete_user(user_id)
    # logout the user

    return redirect(url_for('index.index_page'))






