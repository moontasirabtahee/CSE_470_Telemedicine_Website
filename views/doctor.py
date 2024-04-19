from flask import Flask , request, Blueprint, render_template, redirect, url_for
from controllers import doctor as d
from controllers import profile , user


doctor = Blueprint('doctor', __name__)

"""

├── User (Parent)
│   ├── id (Primary Key)
│   ├── username
│   ├── password
│   ├── role (Patient, Doctor, Admin)
│   ├── email
│   └── phone
├── Profile (Child of User)
│   ├── id (Primary Key)
│   ├── user_id (Foreign Key referencing User.id)
│   ├── first_name
│   ├── last_name
│   ├── date_of_birth
│   ├── gender
│   └── address
├── Doctor (Child of Profile)
│   ├── id (Primary Key)
│   ├── profile_id (Foreign Key referencing Profile.id)
│   ├── specialization
│   ├── location
│   └── availability

"""
@doctor.route('/register', methods=['GET', 'POST'])
def register_doctor():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        gender = request.form.get('gender')
        address = request.form.get('address')
        specialization = request.form.get('specialization')
        location = request.form.get('location')
        availability = request.form.get('availability')
        from datetime import datetime

        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

        user_id = user.create_user(username, password, 'Doctor', email, phone).id
        profile_id = profile.create_profile(user_id, first_name, last_name, date_of_birth,gender,address).id
        d.create_doctor(profile_id, specialization, location, availability)
        return redirect(url_for('index.index_page'))


@doctor.route('/update/<int:id>', methods=['GET', 'POST'])
def update_doctor(id):
    doc = d.get_doctor_by_profile_id(id)
    if request.method == 'POST':
        #update user
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user.update_user(id, username=username, password=password, email=email, phone=phone)
        #update profile
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        gender = request.form.get('gender')
        address = request.form.get('address')
        from datetime import datetime
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        profile.update_profile(id, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                               gender = gender, address=address)

        #update doctor
        specialization = request.form.get('specialization')
        location = request.form.get('location')
        availability = request.form.get('availability')
        d.update_doctor(id, specialization=specialization, location=location, availability=availability)
        return redirect(url_for('index.index_page'))
    else:
        return render_template('update_doctor.html', doctor=doc)

@doctor.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_doctor(id):
    d.delete_doctor(id)
    return redirect(url_for('index.index_page'))






