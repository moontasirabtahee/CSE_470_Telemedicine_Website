#Manage the login logic in the login.py file
# Path: views/login.py

from flask import Flask, request, Blueprint, render_template, redirect, url_for
from controllers import doctor, all_User
from models import db, Doctor, Profile, User, Patient
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from flask_login import current_user
from flask_login import LoginManager, UserMixin
from forms import login as lg


login = Blueprint('login', __name__)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login.route('/login', methods=['GET', 'POST'])
def login_page():
    form = lg.LoginForm()
    #if the user is already logged in, redirect them to the index page
    if current_user.is_authenticated:
        return redirect(url_for('index.index_page'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        #check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            # if the user is a doctor, but in database no doctor is created yet then redirect to the doctor registration page
            if user.role == 'doctor':
                if Doctor.query.filter_by(profile_id=user.profile.id).first() is None:
                    return redirect(url_for('register.register_doctor'))
                else:
                    return redirect(url_for('index.index_page'))
            # if the user is a patient, but in database no patient is created yet then redirect to the patient registration page
            elif user.role == 'patient':
                if Patient.query.filter_by(profile_id=user.profile.id).first() is None:
                    return redirect(url_for('register.register_patient'))
                else:
                    return redirect(url_for('index.index_page'))

        else:
            return 'Invalid username or password'
    return render_template('login.html',form=form)

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index_page'))
