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
    return render_template('patient.html', doctors=doctors)